import { NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server";
import { syncTutorFromGoogle } from "@/lib/auth";

export async function GET(request: Request) {
  const { searchParams, origin } = new URL(request.url);
  const code = searchParams.get("code");
  let next = searchParams.get("next") ?? "/en/tutor/exams";
  if (!next.startsWith("/")) next = "/en/tutor/exams";

  if (!code) {
    return NextResponse.redirect(`${origin}/auth/error?reason=missing_code`);
  }

  const supabase = await createClient();
  const { data, error } = await supabase.auth.exchangeCodeForSession(code);
  if (error || !data.user) {
    return NextResponse.redirect(`${origin}/auth/error?reason=exchange`);
  }

  try {
    await syncTutorFromGoogle(data.user);
  } catch {
    await supabase.auth.signOut();
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
