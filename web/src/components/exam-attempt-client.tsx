"use client";

import { useCallback, useEffect, useMemo, useRef, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { useTranslations } from "next-intl";
import { toast } from "sonner";
import { saveAnswerAction, submitAttemptAction } from "@/actions/student";
import type { AttemptPayload, StudentQuestion } from "@/lib/attempts";
import { Button } from "@/components/ui/button";

function formatMs(ms: number) {
  const total = Math.max(0, Math.floor(ms / 1000));
  const m = Math.floor(total / 60);
  const s = total % 60;
  return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

export function ExamAttemptClient({
  locale,
  token,
  initial,
}: {
  locale: string;
  token: string;
  initial: AttemptPayload;
}) {
  const t = useTranslations("attempt");
  const router = useRouter();
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState(initial.answers);
  const [saveState, setSaveState] = useState<"idle" | "saving" | "saved" | "error">("idle");
  const [remaining, setRemaining] = useState(() =>
    Math.max(0, new Date(initial.attempt.deadline_at).getTime() - Date.now()),
  );
  const [pendingSubmit, startSubmit] = useTransition();
  const expiredOnce = useRef(false);
  const saveTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  const questions = initial.questions;
  const current: StudentQuestion | undefined = questions[index];
  const answeredCount = useMemo(
    () => Object.keys(answers).filter((k) => answers[Number(k)]).length,
    [answers],
  );

  useEffect(() => {
    const tick = () => {
      const ms = Math.max(0, new Date(initial.attempt.deadline_at).getTime() - Date.now());
      setRemaining(ms);
      if (ms <= 0 && !expiredOnce.current) {
        expiredOnce.current = true;
        toast.message(t("expired"));
        const fd = new FormData();
        fd.set("locale", locale);
        fd.set("token", token);
        fd.set("attemptId", initial.attempt.id);
        startSubmit(() => {
          void submitAttemptAction(fd);
        });
      }
    };
    tick();
    const id = setInterval(tick, 1000);
    return () => clearInterval(id);
  }, [initial.attempt.deadline_at, initial.attempt.id, locale, token, t, startSubmit]);

  const persist = useCallback(
    (questionId: number, option: "A" | "B" | "C" | "D") => {
      if (saveTimer.current) clearTimeout(saveTimer.current);
      setSaveState("saving");
      saveTimer.current = setTimeout(async () => {
        const result = await saveAnswerAction({
          attemptId: initial.attempt.id,
          questionId,
          option,
        });
        if (!result.ok) {
          setSaveState("error");
          toast.error(t("saveFailed"));
          if (result.error === "finalized") {
            router.replace(`/${locale}/e/${token}/done`);
          }
          return;
        }
        setSaveState("saved");
      }, 300);
    },
    [initial.attempt.id, locale, token, router, t],
  );

  function selectOption(option: "A" | "B" | "C" | "D") {
    if (!current || remaining <= 0 || pendingSubmit) return;
    setAnswers((prev) => ({ ...prev, [current.id]: option }));
    persist(current.id, option);
  }

  function onSubmit() {
    if (!window.confirm(t("confirmSubmit"))) return;
    const fd = new FormData();
    fd.set("locale", locale);
    fd.set("token", token);
    fd.set("attemptId", initial.attempt.id);
    startSubmit(() => {
      void submitAttemptAction(fd);
    });
  }

  if (!current) {
    return <p className="p-4 text-[var(--muted)]">No questions.</p>;
  }

  const letters = ["A", "B", "C", "D"] as const;

  return (
    <div className="mx-auto flex min-h-[100dvh] max-w-3xl flex-col bg-[var(--paper)]">
      <header
        className="sticky top-0 z-20 border-b border-[var(--line)] bg-[var(--paper)]/95 px-3 py-3 backdrop-blur"
        style={{ paddingTop: "max(0.75rem, env(safe-area-inset-top))" }}
      >
        <div className="flex items-center justify-between gap-3">
          <div>
            <p className="text-xs text-[var(--muted)]">{t("timeLeft")}</p>
            <p
              className={`font-display text-2xl tabular-nums ${remaining < 60_000 ? "text-red-700" : "text-[var(--ink)]"}`}
              aria-live="polite"
            >
              {formatMs(remaining)}
            </p>
          </div>
          <div className="text-right">
            <p className="text-xs text-[var(--muted)]">
              {t("questionOf", { current: index + 1, total: questions.length })}
            </p>
            <p className="text-sm font-medium text-[var(--ink)]">
              {t("answered", { count: answeredCount })}
            </p>
            <p className="text-xs text-[var(--lagoon)]" aria-live="polite">
              {saveState === "saving"
                ? t("saving")
                : saveState === "saved"
                  ? t("saved")
                  : saveState === "error"
                    ? t("saveFailed")
                    : "\u00A0"}
            </p>
          </div>
        </div>

        <div className="mt-3 -mx-1 flex gap-1 overflow-x-auto pb-1 touch-pan-x">
          {questions.map((q, i) => {
            const answered = Boolean(answers[q.id]);
            const active = i === index;
            return (
              <button
                key={q.id}
                type="button"
                onClick={() => setIndex(i)}
                className={`pressable flex h-11 min-w-11 shrink-0 items-center justify-center rounded-md text-sm font-semibold touch-manipulation ${
                  active
                    ? "bg-[var(--ink)] text-white"
                    : answered
                      ? "bg-[var(--lagoon)]/15 text-[var(--ink)]"
                      : "bg-white text-[var(--muted)] border border-[var(--line)]"
                }`}
                aria-label={`Question ${i + 1}`}
                aria-current={active ? "true" : undefined}
              >
                {i + 1}
              </button>
            );
          })}
        </div>
      </header>

      <main className="flex-1 px-4 py-5">
        <p className="text-base leading-relaxed text-[var(--ink)] sm:text-lg">{current.stem}</p>
        <div className="mt-5 space-y-3" role="radiogroup" aria-label={t("questionOf", { current: index + 1, total: questions.length })}>
          {letters.map((letter) => {
            const selected = answers[current.id] === letter;
            return (
              <button
                key={letter}
                type="button"
                role="radio"
                aria-checked={selected}
                aria-label={t("option", { letter })}
                onClick={() => selectOption(letter)}
                disabled={remaining <= 0 || pendingSubmit}
                className={`pressable flex min-h-14 w-full items-start gap-3 rounded-xl border px-4 py-3 text-left text-base touch-manipulation ${
                  selected
                    ? "border-[var(--lagoon)] bg-[var(--lagoon)]/10 text-[var(--ink)]"
                    : "border-[var(--line)] bg-white text-[var(--ink)]"
                }`}
              >
                <span className="mt-0.5 flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-current text-sm font-bold">
                  {letter}
                </span>
                <span className="pt-1 leading-snug">{current.options[letter]}</span>
              </button>
            );
          })}
        </div>
      </main>

      <footer
        className="sticky bottom-0 border-t border-[var(--line)] bg-[var(--paper)]/95 px-3 py-3 backdrop-blur"
        style={{ paddingBottom: "max(0.75rem, env(safe-area-inset-bottom))" }}
      >
        <div className="flex gap-2">
          <Button
            type="button"
            variant="secondary"
            className="min-h-12 flex-1 touch-manipulation"
            disabled={index === 0 || pendingSubmit}
            onClick={() => setIndex((i) => Math.max(0, i - 1))}
          >
            {t("prev")}
          </Button>
          {index < questions.length - 1 ? (
            <Button
              type="button"
              className="min-h-12 flex-1 touch-manipulation"
              disabled={pendingSubmit}
              onClick={() => setIndex((i) => Math.min(questions.length - 1, i + 1))}
            >
              {t("next")}
            </Button>
          ) : (
            <Button
              type="button"
              className="min-h-12 flex-1 touch-manipulation"
              disabled={pendingSubmit || remaining <= 0}
              onClick={onSubmit}
            >
              {pendingSubmit ? t("submitting") : t("submit")}
            </Button>
          )}
        </div>
        {index < questions.length - 1 ? (
          <button
            type="button"
            className="pressable mt-2 w-full min-h-11 rounded-md text-sm font-semibold text-[var(--lagoon)] touch-manipulation"
            disabled={pendingSubmit || remaining <= 0}
            onClick={onSubmit}
          >
            {t("submit")}
          </button>
        ) : null}
      </footer>
    </div>
  );
}
