"use client";

import React from "react";
import { useDroppable } from "@dnd-kit/core";
import { KanbanCard } from "./kanban-card";
import { ScrollArea } from "@/components/ui/scroll-area";

export function KanbanColumn({ 
  id, 
  title, 
  deals 
}: { 
  id: string; 
  title: string; 
  deals: any[] 
}) {
  const { setNodeRef } = useDroppable({
    id,
  });

  return (
    <div className="flex flex-col w-72 min-w-[18rem] bg-slate-100/50 dark:bg-slate-900/50 rounded-lg border p-3">
      <div className="flex items-center justify-between mb-4 px-1">
        <h3 className="font-bold text-sm uppercase tracking-wider text-muted-foreground">
          {title}
        </h3>
        <span className="bg-slate-200 dark:bg-slate-800 text-xs font-semibold px-2 py-0.5 rounded-full">
          {deals.length}
        </span>
      </div>
      <ScrollArea className="flex-1">
        <div ref={setNodeRef} className="min-h-[500px]">
          {deals.map((deal) => (
            <KanbanCard key={deal.id} deal={deal} />
          ))}
        </div>
      </ScrollArea>
    </div>
  );
}
