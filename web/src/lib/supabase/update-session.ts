import { createServerClient } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";
import { getSupabaseEnv } from "@/lib/supabase/env";

export type SessionRefresh = {
  response: NextResponse;
  claims: { sub?: string } | null;
};

/**
 * Refresh the Supabase auth cookie on every matched request.
 * Must return the response that carries any Set-Cookie headers.
 */
export async function updateSession(
  request: NextRequest,
): Promise<SessionRefresh> {
  let supabaseResponse = NextResponse.next({ request });

  let url: string;
  let key: string;
  try {
    ({ url, key } = getSupabaseEnv());
  } catch {
    return { response: supabaseResponse, claims: null };
  }

  const supabase = createServerClient(url, key, {
    cookies: {
      getAll() {
        return request.cookies.getAll();
      },
      setAll(cookiesToSet) {
        cookiesToSet.forEach(({ name, value }) => {
          request.cookies.set(name, value);
        });
        supabaseResponse = NextResponse.next({ request });
        cookiesToSet.forEach(({ name, value, options }) => {
          supabaseResponse.cookies.set(name, value, options);
        });
      },
    },
  });

  // Validates JWT and refreshes when needed. Do not insert logic between
  // createServerClient and getClaims/getUser.
  const { data } = await supabase.auth.getClaims();
  const claims = data?.claims
    ? { sub: typeof data.claims.sub === "string" ? data.claims.sub : undefined }
    : null;

  return { response: supabaseResponse, claims };
}
