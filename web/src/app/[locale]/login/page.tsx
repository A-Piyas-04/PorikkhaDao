import { setRequestLocale } from "next-intl/server";
import { AppShell } from "@/components/app-shell";
import { LoginForm } from "@/components/login-form";

export default async function LoginPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  setRequestLocale(locale);

  return (
    <AppShell locale={locale}>
      <LoginForm locale={locale} />
    </AppShell>
  );
}
