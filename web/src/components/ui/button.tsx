import * as React from "react";
import { cn } from "@/lib/utils";

type Props = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "primary" | "secondary" | "ghost";
};

export function Button({
  className,
  variant = "primary",
  ...props
}: Props) {
  return (
    <button
      className={cn(
        "inline-flex items-center justify-center rounded-md px-4 py-2 text-sm font-semibold transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 disabled:opacity-50",
        variant === "primary" &&
          "bg-[var(--mark)] text-[var(--ink)] hover:brightness-95 focus-visible:outline-[var(--lagoon)]",
        variant === "secondary" &&
          "border border-[var(--line)] bg-white text-[var(--ink)] hover:bg-[var(--mist)] focus-visible:outline-[var(--lagoon)]",
        variant === "ghost" &&
          "text-[var(--ink)] hover:bg-[var(--mist)] focus-visible:outline-[var(--lagoon)]",
        className,
      )}
      {...props}
    />
  );
}
