"use client";

import React from "react";
import { useDraggable } from "@dnd-kit/core";
import { Card, CardContent } from "@/components/ui/card";
import { Building2, User } from "lucide-react";
import { useTranslation } from "@/hooks/use-translation";

export function KanbanCard({ deal }: { deal: any }) {
  const { t } = useTranslation();
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: deal.id,
  });

  const style = transform
    ? {
        transform: `translate3d(${transform.x}px, ${transform.y}px, 0)`,
      }
    : undefined;

  return (
    <div ref={setNodeRef} style={style} {...listeners} {...attributes}>
      <Card className="mb-3 cursor-grab active:cursor-grabbing hover:border-primary transition-colors shadow-sm">
        <CardContent className="p-4">
          <h4 className="font-semibold text-sm mb-2">{deal.title}</h4>
          <div className="flex items-center gap-2 text-xs text-muted-foreground mb-3">
            <Building2 className="h-3 w-3" />
            <span>{deal.company?.name || t("pipeline.noCompany")}</span>
          </div>
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-1 text-xs font-medium text-primary">
              ${deal.value.toLocaleString()}
            </div>
            <div className="flex items-center gap-1 text-xs text-muted-foreground">
              <User className="h-3 w-3" />
              <span>{deal.owner?.name?.split(" ")[0]}</span>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
