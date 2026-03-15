import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { getToken } from "next-auth/jwt";

export async function middleware(req: NextRequest) {
  const token = await getToken({ req, secret: process.env.NEXTAUTH_SECRET });
  const { pathname } = req.nextUrl;

  // Protect dashboard and api routes
  if (pathname.startsWith("/dashboard") || pathname.startsWith("/api/user") || pathname.startsWith("/api/deals")) {
    if (!token) {
      const url = req.nextUrl.clone();
      url.pathname = "/login";
      
      // Keep absolute URL if on tunnel
      if (req.headers.get("host")?.includes("trycloudflare.com")) {
         url.protocol = "https";
         url.host = req.headers.get("host")!;
         url.port = "";
      }
      return NextResponse.redirect(url);
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    "/dashboard/:path*",
    "/api/:path*",
  ],
};
