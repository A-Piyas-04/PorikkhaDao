/** UTC ISO helpers for attempt timing + Bangladesh display. */

export function nowUtcIso(): string {
  return new Date().toISOString();
}

export function addMinutesIso(startIso: string, minutes: number): string {
  const d = new Date(startIso);
  d.setUTCMinutes(d.getUTCMinutes() + minutes);
  return d.toISOString();
}

export function isPastDeadline(deadlineIso: string, nowIso = nowUtcIso()): boolean {
  return new Date(nowIso).getTime() >= new Date(deadlineIso).getTime();
}

export function remainingMs(deadlineIso: string, nowIso = nowUtcIso()): number {
  return Math.max(0, new Date(deadlineIso).getTime() - new Date(nowIso).getTime());
}

const dhakaFormatter = new Intl.DateTimeFormat("en-GB", {
  timeZone: "Asia/Dhaka",
  year: "numeric",
  month: "short",
  day: "2-digit",
  hour: "2-digit",
  minute: "2-digit",
  hour12: true,
});

/** Format a UTC ISO timestamp for Bangladesh display. */
export function formatDhaka(iso: string | null | undefined, locale: string = "en"): string {
  if (!iso) return "—";
  const date = new Date(iso);
  if (Number.isNaN(date.getTime())) return "—";
  if (locale === "bn") {
    return new Intl.DateTimeFormat("bn-BD", {
      timeZone: "Asia/Dhaka",
      year: "numeric",
      month: "short",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      hour12: true,
    }).format(date);
  }
  return dhakaFormatter.format(date);
}
