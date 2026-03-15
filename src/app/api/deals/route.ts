import { prisma } from "@/lib/prisma";
import { NextResponse } from "next/server";

export async function GET() {
  try {
    const deals = await prisma.deal.findMany({
      include: {
        company: true,
        owner: true,
      },
      orderBy: {
        updatedAt: "desc",
      },
    });
    
    console.log(`API Found ${deals.length} deals`);
    return NextResponse.json(deals);
  } catch (error) {
    console.error("Database connection failed:", error);
    return NextResponse.json({ error: "Database error" }, { status: 500 });
  }
}

export async function PATCH(request: Request) {
  try {
    const { id, status } = await request.json();
    
    const updatedDeal = await prisma.deal.update({
      where: { id },
      data: { status },
    });
    
    return NextResponse.json(updatedDeal);
  } catch (error) {
    return NextResponse.json({ error: "Failed to update deal" }, { status: 500 });
  }
}
