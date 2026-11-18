import { NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server";
import { syncAppUser, type AuthIntent } from "@/lib/auth";

export async function GET(request: Request) {
  const { searchParams, origin } = new URL(request.url);
  const code = searchParams.get("code");
  let next = searchParams.get("next") ?? "/";
  if (!next.startsWith("/")) next = "/";

  const intentRaw = searchParams.get("intent") ?? "student";
  const intent: AuthIntent = intentRaw === "tutor" ? "tutor" : "student";

  if (!code) {
    return NextResponse.redirect(`${origin}/auth/error?reason=missing_code`);
  }

  const supabase = await createClient();
  const { data, error } = await supabase.auth.exchangeCodeForSession(code);
  if (error || !data.user) {
    return NextResponse.redirect(`${origin}/auth/error?reason=exchange`);
  }

  try {
    await syncAppUser(data.user, intent);
  } catch (err) {
    await supabase.auth.signOut();
    const message = err instanceof Error ? err.message : "";
    if (message === "NOT_TUTOR") {
      return NextResponse.redirect(`${origin}/auth/error?reason=not_tutor`);
    }
    if (message === "EMAIL_IS_TUTOR") {
      return NextResponse.redirect(`${origin}/auth/error?reason=tutor_email`);
    }
    return NextResponse.redirect(`${origin}/auth/error?reason=sync`);
  }

  const forwardedHost = request.headers.get("x-forwarded-host");
  const isLocalEnv = process.env.NODE_ENV === "development";
  if (isLocalEnv) {
    return NextResponse.redirect(`${origin}${next}`);
  }
  if (forwardedHost) {
    return NextResponse.redirect(`https://${forwardedHost}${next}`);
  }
  return NextResponse.redirect(`${origin}${next}`);
}
