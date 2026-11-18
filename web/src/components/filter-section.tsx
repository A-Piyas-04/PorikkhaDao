"use client";

import type { ReactNode } from "react";
import { ChevronDown } from "lucide-react";
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";
import { cn } from "@/lib/utils";

type FilterSectionProps = {
  title: string;
  summary?: string;
  open: boolean;
  onOpenChange: (open: boolean) => void;
  selectAllLabel: string;
  deselectAllLabel: string;
  onSelectAll?: () => void;
  onDeselectAll?: () => void;
  canSelectAll?: boolean;
  canDeselectAll?: boolean;
  hint?: string;
  empty?: ReactNode;
  children?: ReactNode;
  className?: string;
  nested?: boolean;
};

export function FilterSection({
  title,
  summary,
  open,
  onOpenChange,
  selectAllLabel,
  deselectAllLabel,
  onSelectAll,
  onDeselectAll,
  canSelectAll = true,
  canDeselectAll = true,
  hint,
  empty,
  children,
  className,
  nested = false,
}: FilterSectionProps) {
  return (
    <Collapsible
      open={open}
      onOpenChange={onOpenChange}
      className={cn(
        "rounded-lg border border-[var(--line)] bg-white/90",
        nested && "border-[var(--line)]/80 bg-[var(--mist)]/40",
        className,
      )}
    >
      <div
        className={cn(
          "flex flex-wrap items-center gap-2 px-3 py-2.5",
          nested ? "px-2.5 py-2" : "sm:px-4",
        )}
      >
        <CollapsibleTrigger
          type="button"
          className="pressable group flex min-h-11 min-w-0 flex-1 items-center gap-2 rounded-md text-left touch-manipulation focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--lagoon)]"
        >
          <ChevronDown
            className={cn(
              "h-4 w-4 shrink-0 text-[var(--muted)] transition-transform duration-200",
              open ? "rotate-0" : "-rotate-90",
            )}
            aria-hidden
          />
          <span className="min-w-0">
            <span
              className={cn(
                "block font-semibold text-[var(--ink)]",
                nested ? "text-sm" : "text-sm sm:text-base",
              )}
            >
              {title}
            </span>
            {summary ? (
              <span className="block text-xs text-[var(--muted)]">{summary}</span>
            ) : null}
          </span>
        </CollapsibleTrigger>

        <div className="flex shrink-0 items-center gap-1">
          {onSelectAll ? (
            <button
              type="button"
              disabled={!canSelectAll}
              onClick={onSelectAll}
              className="pressable min-h-9 rounded-md px-2.5 text-xs font-semibold text-[var(--lagoon)] touch-manipulation hover:bg-[var(--mist)] disabled:pointer-events-none disabled:opacity-40"
            >
              {selectAllLabel}
            </button>
          ) : null}
          {onDeselectAll ? (
            <button
              type="button"
              disabled={!canDeselectAll}
              onClick={onDeselectAll}
              className="pressable min-h-9 rounded-md px-2.5 text-xs font-semibold text-[var(--muted)] touch-manipulation hover:bg-[var(--mist)] disabled:pointer-events-none disabled:opacity-40"
            >
              {deselectAllLabel}
            </button>
          ) : null}
        </div>
      </div>

      <CollapsibleContent>
        <div
          className={cn(
            "space-y-3 border-t border-[var(--line)] px-3 py-3",
            nested ? "px-2.5 py-2.5" : "sm:px-4",
          )}
        >
          {hint ? <p className="text-sm text-[var(--muted)]">{hint}</p> : null}
          {empty ?? children}
        </div>
      </CollapsibleContent>
    </Collapsible>
  );
}

export function FilterCheckItem({
  checked,
  onChange,
  label,
  name,
  value,
}: {
  checked: boolean;
  onChange: () => void;
  label: string;
  name?: string;
  value?: string;
}) {
  return (
    <label className="flex min-h-11 items-start gap-2 rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm touch-manipulation">
      <input
        type="checkbox"
        name={name}
        value={value}
        checked={checked}
        onChange={onChange}
        className="mt-1"
      />
      <span className="leading-snug text-[var(--ink)]">{label}</span>
    </label>
  );
}
