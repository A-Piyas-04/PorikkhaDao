"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireTutor } from "@/lib/auth";
import { countEligible, type EligibilityFilters } from "@/lib/eligibility";
import { createExamDraft, publishExam } from "@/lib/exams";

export type CreateExamState = {
  error?: string;
  eligibleCount?: number;
};

function parseFilters(formData: FormData): EligibilityFilters & {
  requestedCount: number;
  durationMinutes: number;
  title: string;
  locale: string;
} {
  const topicIds = formData
    .getAll("topicIds")
    .map((v) => String(v))
    .filter(Boolean);
  const difficulty = String(formData.get("difficulty") ?? "") as EligibilityFilters["difficulty"];
  const qtype = String(formData.get("qtype") ?? "") as EligibilityFilters["qtype"];

  return {
    topicIds,
    difficulty: difficulty || "",
    qtype: qtype || "",
    requestedCount: Number(formData.get("count") ?? 0),
    durationMinutes: Number(formData.get("duration") ?? 0),
    title: String(formData.get("title") ?? ""),
    locale: String(formData.get("locale") ?? "en"),
  };
}

export async function getEligibleCountAction(input: {
  topicIds: string[];
  difficulty?: string;
  qtype?: string;
}): Promise<number> {
  await requireTutor();
  return countEligible({
    topicIds: input.topicIds,
    difficulty: (input.difficulty as EligibilityFilters["difficulty"]) || "",
    qtype: (input.qtype as EligibilityFilters["qtype"]) || "",
  });
}

export async function createExamAction(
  _prev: CreateExamState,
  formData: FormData,
): Promise<CreateExamState> {
  const parsed = parseFilters(formData);
  const tutor = await requireTutor(parsed.locale);

  if (!parsed.title.trim()) return { error: "title" };
  if (parsed.topicIds.length < 1) return { error: "topics" };
  if (!Number.isFinite(parsed.requestedCount) || parsed.requestedCount < 1) {
    return { error: "count" };
  }
  if (!Number.isFinite(parsed.durationMinutes) || parsed.durationMinutes < 1) {
    return { error: "duration" };
  }

  const filters: EligibilityFilters = {
    topicIds: parsed.topicIds,
    difficulty: parsed.difficulty,
    qtype: parsed.qtype,
  };
  const eligibleCount = await countEligible(filters);

  try {
    const { examId } = await createExamDraft({
      ownerId: tutor.id,
      title: parsed.title,
      durationMinutes: parsed.durationMinutes,
      settings: {
        ...filters,
        requestedCount: parsed.requestedCount,
      },
    });
    revalidatePath(`/${parsed.locale}/tutor/exams`);
    redirect(`/${parsed.locale}/tutor/exams/${examId}`);
  } catch (err) {
    if (
      typeof err === "object" &&
      err &&
      "digest" in err &&
      String((err as { digest?: string }).digest).startsWith("NEXT_REDIRECT")
    ) {
      throw err;
    }
    const message = err instanceof Error ? err.message : "";
    if (message.startsWith("NOT_ENOUGH:")) {
      return {
        error: "not_enough",
        eligibleCount: Number(message.split(":")[1] ?? eligibleCount),
      };
    }
    if (message === "UNAUTHORIZED") return { error: "auth" };
    throw err;
  }
}

export async function publishExamAction(formData: FormData) {
  const examId = String(formData.get("examId") ?? "");
  const locale = String(formData.get("locale") ?? "en");
  const tutor = await requireTutor(locale);
  await publishExam(examId, tutor.id);
  revalidatePath(`/${locale}/tutor/exams`);
  revalidatePath(`/${locale}/tutor/exams/${examId}`);
  redirect(`/${locale}/tutor/exams/${examId}?published=1`);
}
