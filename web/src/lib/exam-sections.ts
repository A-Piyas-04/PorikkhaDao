import {
  pickRandomEligible,
  type EligibilityFilters,
} from "@/lib/eligibility";
import { ensureDb, sql } from "@/db";

export type ExamScope = {
  subjectIds: string[];
  paperIds: string[];
  chapterIds: string[];
};

export type ExamSection = {
  key: string;
  subjectId: string;
  paperId: string | null;
  labelEn: string;
  labelBn: string;
  startOrder: number;
  endOrder: number;
  count: number;
};

type TopicAncestry = {
  topic_id: string;
  chapter_id: string;
  paper_id: string;
  subject_id: string;
  paper_number: number;
  subject_name_en: string;
  subject_name_bn: string;
  paper_name_en: string;
  paper_name_bn: string;
};

type LeafPool = {
  key: string;
  subjectId: string;
  paperId: string;
  topicIds: string[];
  labelEn: string;
  labelBn: string;
};

/** Split `total` across `n` parts; remainder goes to the first parts. */
export function allocateCounts(total: number, n: number): number[] {
  if (n <= 0) return [];
  if (n === 1) return [total];
  const base = Math.floor(total / n);
  const rem = total % n;
  return Array.from({ length: n }, (_, i) => base + (i < rem ? 1 : 0));
}

async function loadTopicAncestry(topicIds: string[]): Promise<TopicAncestry[]> {
  if (topicIds.length === 0) return [];
  await ensureDb();
  const db = sql();
  const rows = await db`
    SELECT
      t.id AS topic_id,
      t.chapter_id,
      c.paper_id,
      p.subject_id,
      p.number AS paper_number,
      s.name_en AS subject_name_en,
      s.name_bn AS subject_name_bn,
      p.name_en AS paper_name_en,
      p.name_bn AS paper_name_bn
    FROM topics t
    JOIN chapters c ON c.id = t.chapter_id
    JOIN papers p ON p.id = c.paper_id
    JOIN subjects s ON s.id = p.subject_id
    WHERE t.id IN ${db(topicIds)}
  `;
  return rows as unknown as TopicAncestry[];
}

function leafLabel(
  multiSubject: boolean,
  papersInSubject: number,
  ancestry: TopicAncestry,
): { labelEn: string; labelBn: string } {
  const multiPaper = papersInSubject > 1;
  if (!multiSubject && multiPaper) {
    return {
      labelEn: ancestry.paper_name_en,
      labelBn: ancestry.paper_name_bn,
    };
  }
  if (multiSubject && !multiPaper) {
    return {
      labelEn: ancestry.subject_name_en,
      labelBn: ancestry.subject_name_bn,
    };
  }
  if (multiSubject && multiPaper) {
    return {
      labelEn: `${ancestry.subject_name_en} — ${ancestry.paper_name_en}`,
      labelBn: `${ancestry.subject_name_bn} — ${ancestry.paper_name_bn}`,
    };
  }
  return {
    labelEn: ancestry.subject_name_en,
    labelBn: ancestry.subject_name_bn,
  };
}

/**
 * Build ordered leaf pools from selected topics + scope.
 * Multiple chapters in the same paper collapse into one shuffled pool.
 */
export async function buildLeafPools(
  topicIds: string[],
  scope: ExamScope,
): Promise<LeafPool[]> {
  const ancestry = await loadTopicAncestry(topicIds);
  if (ancestry.length === 0) return [];

  const byTopic = new Map(ancestry.map((row) => [row.topic_id, row]));
  const chapterSet = new Set(scope.chapterIds);
  const paperSet = new Set(scope.paperIds);
  const subjectOrder = scope.subjectIds.filter(Boolean);

  const topicsByPaper = new Map<string, string[]>();
  const paperMeta = new Map<string, TopicAncestry>();

  for (const topicId of topicIds) {
    const row = byTopic.get(topicId);
    if (!row) continue;
    if (chapterSet.size > 0 && !chapterSet.has(row.chapter_id)) continue;
    if (paperSet.size > 0 && !paperSet.has(row.paper_id)) continue;
    const list = topicsByPaper.get(row.paper_id) ?? [];
    list.push(topicId);
    topicsByPaper.set(row.paper_id, list);
    paperMeta.set(row.paper_id, row);
  }

  const papersBySubject = new Map<string, string[]>();
  for (const [paperId, meta] of paperMeta) {
    if (!topicsByPaper.has(paperId)) continue;
    const list = papersBySubject.get(meta.subject_id) ?? [];
    list.push(paperId);
    papersBySubject.set(meta.subject_id, list);
  }

  for (const [subjectId, paperIds] of papersBySubject) {
    paperIds.sort((a, b) => {
      const na = paperMeta.get(a)?.paper_number ?? 0;
      const nb = paperMeta.get(b)?.paper_number ?? 0;
      return na - nb;
    });
    papersBySubject.set(subjectId, paperIds);
  }

  const orderedSubjects =
    subjectOrder.length > 0
      ? subjectOrder.filter((id) => papersBySubject.has(id))
      : [...papersBySubject.keys()];

  const multiSubject = orderedSubjects.length > 1;
  const leaves: LeafPool[] = [];

  for (const subjectId of orderedSubjects) {
    const paperIds = papersBySubject.get(subjectId) ?? [];
    for (const paperId of paperIds) {
      const poolTopics = topicsByPaper.get(paperId) ?? [];
      if (poolTopics.length === 0) continue;
      const meta = paperMeta.get(paperId)!;
      const labels = leafLabel(multiSubject, paperIds.length, meta);
      leaves.push({
        key: `${subjectId}:${paperId}`,
        subjectId,
        paperId,
        topicIds: poolTopics,
        labelEn: labels.labelEn,
        labelBn: labels.labelBn,
      });
    }
  }

  return leaves;
}

/** Hierarchical count allocation: subjects first, then papers within each subject. */
export function allocateLeafCounts(
  total: number,
  leaves: LeafPool[],
): number[] {
  if (leaves.length === 0) return [];
  if (leaves.length === 1) return [total];

  const subjectIds: string[] = [];
  for (const leaf of leaves) {
    if (!subjectIds.includes(leaf.subjectId)) subjectIds.push(leaf.subjectId);
  }

  const counts = new Array<number>(leaves.length).fill(0);

  if (subjectIds.length === 1) {
    const paperCounts = allocateCounts(total, leaves.length);
    for (let i = 0; i < leaves.length; i += 1) counts[i] = paperCounts[i];
    return counts;
  }

  const subjectTotals = allocateCounts(total, subjectIds.length);
  let leafIndex = 0;
  for (let s = 0; s < subjectIds.length; s += 1) {
    const subjectId = subjectIds[s];
    const start = leafIndex;
    while (leafIndex < leaves.length && leaves[leafIndex].subjectId === subjectId) {
      leafIndex += 1;
    }
    const span = leafIndex - start;
    const paperCounts = allocateCounts(subjectTotals[s], span);
    for (let i = 0; i < span; i += 1) {
      counts[start + i] = paperCounts[i];
    }
  }
  return counts;
}

export async function pickSectionedQuestions(
  filters: EligibilityFilters,
  requestedCount: number,
  scope: ExamScope,
): Promise<{ questionIds: number[]; sections: ExamSection[] }> {
  const leaves = await buildLeafPools(filters.topicIds, scope);
  if (leaves.length === 0) {
    throw new Error("NO_TOPICS");
  }

  if (leaves.length === 1) {
    const questionIds = await pickRandomEligible(filters, requestedCount);
    return { questionIds, sections: [] };
  }

  const counts = allocateLeafCounts(requestedCount, leaves);
  const questionIds: number[] = [];
  const sections: ExamSection[] = [];
  let order = 1;

  for (let i = 0; i < leaves.length; i += 1) {
    const leaf = leaves[i];
    const count = counts[i];
    if (count < 1) continue;

    const ids = await pickRandomEligible(
      {
        topicIds: leaf.topicIds,
        difficulty: filters.difficulty,
        qtype: filters.qtype,
      },
      count,
    );

    const startOrder = order;
    const endOrder = order + ids.length - 1;
    questionIds.push(...ids);
    sections.push({
      key: leaf.key,
      subjectId: leaf.subjectId,
      paperId: leaf.paperId,
      labelEn: leaf.labelEn,
      labelBn: leaf.labelBn,
      startOrder,
      endOrder,
      count: ids.length,
    });
    order = endOrder + 1;
  }

  return { questionIds, sections };
}

export function sectionLabelForOrder(
  sections: ExamSection[] | undefined,
  order: number,
  locale: string,
): string | null {
  if (!sections || sections.length === 0) return null;
  const section = sections.find(
    (s) => order >= s.startOrder && order <= s.endOrder,
  );
  if (!section) return null;
  return locale === "bn" ? section.labelBn : section.labelEn;
}

export function isSectionStart(
  sections: ExamSection[] | undefined,
  order: number,
): ExamSection | null {
  if (!sections || sections.length === 0) return null;
  return sections.find((s) => s.startOrder === order) ?? null;
}
