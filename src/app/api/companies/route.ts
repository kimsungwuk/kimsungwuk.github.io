import { prisma } from "@/lib/prisma";
import { NextResponse } from "next/server";

export async function GET() {
  try {
    const companies = await prisma.company.findMany({
      orderBy: { createdAt: "desc" },
    });
    return NextResponse.json(companies);
  } catch (error) {
    console.error("Database connection failed for companies");
    return NextResponse.json({ error: "Database error" }, { status: 500 });
  }
}
