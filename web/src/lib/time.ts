/** UTC ISO helpers for attempt timing. */

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
