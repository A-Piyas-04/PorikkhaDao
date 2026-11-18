"use client";

import { useEffect, useState } from "react";
import { cn } from "@/lib/utils";

export function RouteProgress({
  label,
  className,
  fullscreen = false,
}: {
  label: string;
  className?: string;
  fullscreen?: boolean;
}) {
  const [progress, setProgress] = useState(8);

  useEffect(() => {
    const started = Date.now();
    const id = window.setInterval(() => {
      const elapsed = Date.now() - started;
      // Ease toward ~92% while waiting; never hit 100% until unmount.
      const next =
        elapsed < 400
          ? 8 + (elapsed / 400) * 28
          : elapsed < 1600
            ? 36 + ((elapsed - 400) / 1200) * 40
            : Math.min(92, 76 + ((elapsed - 1600) / 4000) * 16);
      setProgress(next);
    }, 80);
    return () => window.clearInterval(id);
  }, []);

  return (
    <div
      className={cn(
        "flex flex-col items-center justify-center gap-5 px-6 text-center",
        fullscreen
          ? "fixed inset-0 z-50 bg-[var(--paper)]/92 backdrop-blur-sm"
          : "min-h-[50vh] rounded-xl border border-[var(--line)] bg-white/80 py-16 shadow-sm",
        className,
      )}
      role="status"
      aria-live="polite"
      aria-busy="true"
    >
      <div className="w-full max-w-sm space-y-3">
        <p className="font-display text-2xl text-[var(--ink)]">{label}</p>
        <div
          className="h-2.5 overflow-hidden rounded-full bg-[var(--mist)]"
          aria-hidden
        >
          <div
            className="h-full rounded-full bg-[var(--lagoon)] transition-[width] duration-150 ease-out"
            style={{ width: `${progress}%` }}
          />
        </div>
        <p className="text-sm tabular-nums text-[var(--muted)]">
          {Math.round(progress)}%
        </p>
      </div>
    </div>
  );
}
