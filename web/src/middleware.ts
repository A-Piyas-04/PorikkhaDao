import createMiddleware from "next-intl/middleware";
import { NextRequest, NextResponse } from "next/server";
import { routing } from "@/i18n/routing";

const intlMiddleware = createMiddleware(routing);

export default function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const localeMatch = pathname.match(/^\/(en|bn)(\/|$)/);
  const locale = localeMatch?.[1] ?? "en";
  const pathWithoutLocale = localeMatch
    ? pathname.slice(locale.length + 1) || "/"
    : pathname;

  const isTutorRoute = pathWithoutLocale.startsWith("/tutor");
  const session = request.cookies.get("porikkhadao_session")?.value;

  if (isTutorRoute && !session) {
    const url = request.nextUrl.clone();
    url.pathname = `/${locale}/login`;
    return NextResponse.redirect(url);
  }

  if (pathWithoutLocale === "/login" && session) {
    const url = request.nextUrl.clone();
    url.pathname = `/${locale}/tutor/exams`;
    return NextResponse.redirect(url);
  }

  return intlMiddleware(request);
}

export const config = {
  matcher: ["/", "/(bn|en)/:path*"],
};
