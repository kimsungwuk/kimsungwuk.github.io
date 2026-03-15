"use client";

import React, { useState, useEffect } from "react";
import {
  DndContext,
  DragOverlay,
  closestCorners,
  KeyboardSensor,
  PointerSensor,
  useSensor,
  useSensors,
  DragStartEvent,
  DragEndEvent,
} from "@dnd-kit/core";
import { KanbanColumn } from "./kanban-column";
import { KanbanCard } from "./kanban-card";
import { DealStatus } from "@prisma/client";
import { useTranslation } from "@/hooks/use-translation";

export function KanbanBoard() {
  const { t } = useTranslation();
  const [deals, setDeals] = useState<any[]>([]);
  const [activeId, setActiveId] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  const STAGES = [
    { id: DealStatus.LEAD, title: t("pipeline.stages.lead") },
    { id: DealStatus.MEETING, title: t("pipeline.stages.meeting") },
    { id: DealStatus.PROPOSAL, title: t("pipeline.stages.proposal") },
    { id: DealStatus.CONTRACT, title: t("pipeline.stages.contract") },
  ];

  const sensors = useSensors(
    useSensor(PointerSensor, {
      activationConstraint: {
        distance: 5,
      },
    }),
    useSensor(KeyboardSensor)
  );

  useEffect(() => {
    fetchDeals();
  }, []);

  const fetchDeals = async () => {
    try {
      const response = await fetch("/api/deals");
      const data = await response.json();
      setDeals(data);
      setIsLoading(false);
    } catch (error) {
      console.error("Error fetching deals:", error);
      setIsLoading(false);
    }
  };

  const handleDragStart = (event: DragStartEvent) => {
    setActiveId(event.active.id as string);
  };

  const handleDragEnd = async (event: DragEndEvent) => {
    const { active, over } = event;
    setActiveId(null);

    if (!over) return;

    const dealId = active.id as string;
    const newStatus = over.id as DealStatus;

    // Find the deal to update locally
    const deal = deals.find((d) => d.id === dealId);
    if (!deal || deal.status === newStatus) return;

    // Optimistic UI update
    setDeals(
      deals.map((d) => (d.id === dealId ? { ...d, status: newStatus } : d))
    );

    // Persist to DB
    try {
      await fetch("/api/deals", {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: dealId, status: newStatus }),
      });
    } catch (error) {
      console.error("Error updating deal status:", error);
      // Rollback on error
      fetchDeals();
    }
  };

  if (isLoading) {
    return <div className="flex h-96 items-center justify-center">Loading pipeline...</div>;
  }

  const activeDeal = activeId ? deals.find((d) => d.id === activeId) : null;

  return (
    <DndContext
      sensors={sensors}
      collisionDetection={closestCorners}
      onDragStart={handleDragStart}
      onDragEnd={handleDragEnd}
    >
      <div className="flex gap-6 h-full overflow-x-auto pb-4 min-h-[calc(100vh-12rem)]">
        {STAGES.map((stage) => (
          <KanbanColumn
            key={stage.id}
            id={stage.id}
            title={stage.title}
            deals={deals.filter((deal) => deal.status === stage.id)}
          />
        ))}
      </div>

      <DragOverlay>
        {activeId ? <KanbanCard deal={activeDeal} /> : null}
      </DragOverlay>
    </DndContext>
  );
}
