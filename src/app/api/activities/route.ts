import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json([
    { id: "act-1", type: "CALL", content: "Initial discovery call with Acme Corp", createdAt: new Date().toISOString() },
    { id: "act-2", type: "MEETING", content: "Product demo for Global Tech team", createdAt: new Date().toISOString() }
  ]);
}
