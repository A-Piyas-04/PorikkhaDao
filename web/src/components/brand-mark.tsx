import { cn } from "@/lib/utils";

type Props = {
  className?: string;
  title?: string;
};

/** PorikkhaDao mark: exam sheet with a selected MCQ. */
export function BrandMark({ className, title = "PorikkhaDao" }: Props) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 64 64"
      fill="none"
      className={cn("shrink-0", className)}
      role="img"
      aria-label={title}
    >
      <rect width="64" height="64" rx="16" fill="#102a43" />
      <path
        d="M16 14h26a4 4 0 0 1 4 4v32a4 4 0 0 1-4 4H16a4 4 0 0 1-4-4V18a4 4 0 0 1 4-4Z"
        fill="#F3F6F8"
      />
      <path d="M38 14l8 8h-5a3 3 0 0 1-3-3V14Z" fill="#C9D6DE" />
      <path
        d="M38 14v5a3 3 0 0 0 3 3h5"
        stroke="#0F766E"
        strokeWidth="1.5"
        strokeLinejoin="round"
      />
      <path
        d="M28 24h14M28 32h14M28 40h10"
        stroke="#C9D6DE"
        strokeWidth="2"
        strokeLinecap="round"
      />
      <circle cx="21" cy="24" r="3.2" stroke="#0F766E" strokeWidth="1.6" />
      <circle cx="21" cy="32" r="3.2" fill="#0F766E" />
      <circle cx="21" cy="40" r="3.2" stroke="#0F766E" strokeWidth="1.6" />
      <path
        d="M19.2 32.1l1.4 1.5 2.8-3.2"
        stroke="#E2B93D"
        strokeWidth="1.8"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}
