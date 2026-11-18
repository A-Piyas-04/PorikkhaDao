import { setRequestLocale } from "next-intl/server";
import { AppShell } from "@/components/app-shell";
import { LoginForm } from "@/components/login-form";

export default async function LoginPage({
  params,
  searchParams,
}: {
  params: Promise<{ locale: string }>;
  searchParams: Promise<{ error?: string }>;
}) {
  const { locale } = await params;
  const { error } = await searchParams;
  setRequestLocale(locale);

  return (
    <AppShell locale={locale}>
      <LoginForm locale={locale} error={error} />
    </AppShell>
  );
}
