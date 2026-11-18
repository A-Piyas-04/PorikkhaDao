import type { Metadata } from "next";
import { Fraunces, Source_Sans_3, Noto_Sans_Bengali } from "next/font/google";
import { Toaster } from "sonner";
import "./globals.css";

const display = Fraunces({
  variable: "--font-display",
  subsets: ["latin"],
});

const body = Source_Sans_3({
  variable: "--font-body",
  subsets: ["latin"],
});

const bengali = Noto_Sans_Bengali({
  variable: "--font-bn",
  subsets: ["bengali"],
  weight: ["400", "500", "600", "700"],
});

export const metadata: Metadata = {
  title: {
    default: "PorikkhaDao",
    template: "%s · PorikkhaDao",
  },
  description: "Topic-precise HSC MCQ exams for tutors",
  applicationName: "PorikkhaDao",
  icons: {
    icon: [{ url: "/brand/porikkhadao-mark.svg", type: "image/svg+xml" }],
    apple: [{ url: "/brand/porikkhadao-mark.svg" }],
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html
      lang="en"
      className={`${display.variable} ${body.variable} ${bengali.variable} h-full antialiased`}
    >
      <body
        className="min-h-full"
        style={{ fontFamily: "var(--font-body), var(--font-bn), sans-serif" }}
      >
        {children}
        <Toaster richColors position="top-center" />
      </body>
    </html>
  );
}
