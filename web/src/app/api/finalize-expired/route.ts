import { NextResponse } from "next/server";
import { finalizeAllExpired } from "@/lib/attempts";
import { getDb } from "@/db";

export const dynamic = "force-dynamic";

export async function POST() {
  // Ensure migrations ran
  getDb();
  const count = finalizeAllExpired();
  return NextResponse.json({ finalized: count });
}

export async function GET() {
  getDb();
  const count = finalizeAllExpired();
  return NextResponse.json({ finalized: count });
}
