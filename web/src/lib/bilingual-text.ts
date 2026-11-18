import type { QuestionRow } from "@/lib/eligibility";

/**
 * Stored MCQ text is authored as English + "\\n" + Bangla (see question bank export).
 * Pick one language for display based on UI locale.
 */
export function pickBilingualText(raw: string, locale: string): string {
  const text = String(raw ?? "");
  const newline = text.indexOf("\n");
  if (newline < 0) return text.trim();

  const first = text.slice(0, newline).trim();
  const rest = text.slice(newline + 1).trim();
  if (!rest) return first;
  if (!first) return rest;

  return locale === "bn" ? rest : first;
}

export function localizeQuestion(
  row: QuestionRow,
  locale: string,
): QuestionRow {
  return {
    ...row,
    stem: pickBilingualText(row.stem, locale),
    option_a: pickBilingualText(row.option_a, locale),
    option_b: pickBilingualText(row.option_b, locale),
    option_c: pickBilingualText(row.option_c, locale),
    option_d: pickBilingualText(row.option_d, locale),
  };
}
