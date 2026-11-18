import Link from "next/link";
import { BrandMark } from "@/components/brand-mark";

const REASONS: Record<string, string> = {
  missing_code: "Google sign-in did not return an auth code. Try again.",
  exchange: "Could not complete Google sign-in. Try again.",
  sync: "Signed in with Google, but we could not create your tutor profile.",
};

export default async function AuthErrorPage({
  searchParams,
}: {
  searchParams: Promise<{ reason?: string }>;
}) {
  const { reason } = await searchParams;
  const message =
    REASONS[reason ?? ""] ?? "Something went wrong during sign-in.";

  return (
    <main className="mx-auto flex min-h-screen max-w-lg flex-col justify-center gap-5 px-4">
      <BrandMark className="h-12 w-12" />
      <h1 className="font-display text-3xl text-[var(--ink)]">Sign-in problem</h1>
      <p className="text-[var(--muted)]">{message}</p>
      <div className="flex gap-4 text-sm">
        <Link href="/en/login" className="font-semibold text-[var(--lagoon)]">
          Tutor login
        </Link>
        <Link href="/en" className="text-[var(--muted)]">
          Home
        </Link>
      </div>
    </main>
  );
}
