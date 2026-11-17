import { setRequestLocale } from "next-intl/server";
import { AppShell } from "@/components/app-shell";

export default async function TutorLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  setRequestLocale(locale);

  return (
    <AppShell locale={locale} showTutorNav>
      {children}
    </AppShell>
  );
}
