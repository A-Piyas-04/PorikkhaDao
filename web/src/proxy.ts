import createMiddleware from "next-intl/middleware";
import { NextRequest, NextResponse } from "next/server";
import { routing } from "@/i18n/routing";
import { updateSession } from "@/lib/supabase/update-session";

const intlMiddleware = createMiddleware(routing);

function copyCookies(from: NextResponse, to: NextResponse) {
  from.cookies.getAll().forEach((cookie) => {
    to.cookies.set(cookie.name, cookie.value);
  });
}

export async function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // Auth callback / error stay outside the locale tree.
  if (pathname.startsWith("/auth")) {
    const { response } = await updateSession(request);
    return response;
  }

  const { response: sessionResponse, claims } = await updateSession(request);

  const localeMatch = pathname.match(/^\/(en|bn)(\/|$)/);
  const locale = localeMatch?.[1] ?? "en";
  const pathWithoutLocale = localeMatch
    ? pathname.slice(locale.length + 1) || "/"
    : pathname;

  const isTutorRoute = pathWithoutLocale.startsWith("/tutor");
  const signedIn = Boolean(claims?.sub);

  if (isTutorRoute && !signedIn) {
    const url = request.nextUrl.clone();
    url.pathname = `/${locale}/login`;
    const redirectResponse = NextResponse.redirect(url);
    copyCookies(sessionResponse, redirectResponse);
    return redirectResponse;
  }

  const intlResponse = intlMiddleware(request);
  copyCookies(sessionResponse, intlResponse);
  return intlResponse;
}

export const config = {
  matcher: ["/", "/(bn|en)/:path*", "/auth/:path*"],
};
