import { NextResponse } from "next/server";
import { finalizeAllExpired } from "@/lib/attempts";
import { ensureDb } from "@/db";

export const dynamic = "force-dynamic";

export async function POST() {
  await ensureDb();
  const count = await finalizeAllExpired();
  return NextResponse.json({ finalized: count });
}

export async function GET() {
  await ensureDb();
  const count = await finalizeAllExpired();
  return NextResponse.json({ finalized: count });
}
