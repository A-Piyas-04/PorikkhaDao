import { Link } from "@/i18n/navigation";
import { BrandMark } from "@/components/brand-mark";
import { cn } from "@/lib/utils";

type Props = {
  locale: string;
  brand: string;
  tagline?: string;
  href?: "/" | string;
  size?: "sm" | "lg";
  className?: string;
};

export function BrandLockup({
  locale,
  brand,
  tagline,
  href = "/",
  size = "sm",
  className,
}: Props) {
  const markClass = size === "lg" ? "h-14 w-14 sm:h-16 sm:w-16" : "h-10 w-10";
  const titleClass =
    size === "lg"
      ? "font-display text-4xl leading-none tracking-tight text-[var(--ink)] sm:text-5xl"
      : "font-display text-2xl leading-none tracking-tight text-[var(--ink)]";

  const content = (
    <>
      <BrandMark className={markClass} title={brand} />
      <span className="min-w-0">
        <span className={cn("block", titleClass)}>{brand}</span>
        {tagline ? (
          <span
            className={cn(
              "mt-1 block text-[var(--muted)]",
              size === "lg"
                ? "text-base sm:text-lg"
                : "hidden text-sm sm:block",
            )}
          >
            {tagline}
          </span>
        ) : null}
      </span>
    </>
  );

  if (!href) {
    return (
      <div className={cn("inline-flex items-center gap-3", className)} lang={locale}>
        {content}
      </div>
    );
  }

  return (
    <Link
      href={href as "/"}
      className={cn(
        "inline-flex items-center gap-3 rounded-md outline-offset-4 focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--lagoon)]",
        className,
      )}
      lang={locale}
    >
      {content}
    </Link>
  );
}
