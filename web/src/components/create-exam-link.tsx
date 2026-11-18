"use client";

import { useState } from "react";
import { useTranslations } from "next-intl";
import { Link } from "@/i18n/navigation";
import { buttonClassName, type ButtonVariant } from "@/components/ui/button";
import { RouteProgress } from "@/components/route-progress";
import { cn } from "@/lib/utils";

export function CreateExamLink({
  children,
  variant = "primary",
  className,
  plain = false,
}: {
  children: React.ReactNode;
  variant?: ButtonVariant;
  className?: string;
  plain?: boolean;
}) {
  const t = useTranslations("create");
  const [loading, setLoading] = useState(false);

  return (
    <>
      {loading ? <RouteProgress label={t("loading")} fullscreen /> : null}
      <Link
        href="/tutor/exams/new"
        className={
          plain
            ? cn(className)
            : buttonClassName(variant, className)
        }
        onClick={() => setLoading(true)}
        aria-busy={loading}
      >
        {children}
      </Link>
    </>
  );
}
