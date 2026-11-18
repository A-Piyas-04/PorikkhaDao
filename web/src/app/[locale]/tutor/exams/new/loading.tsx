"use client";

import { useTranslations } from "next-intl";
import { RouteProgress } from "@/components/route-progress";

export default function NewExamLoading() {
  const t = useTranslations("create");
  return <RouteProgress label={t("loading")} />;
}
