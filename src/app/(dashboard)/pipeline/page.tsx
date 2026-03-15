"use client";

import { KanbanBoard } from "@/components/pipeline/kanban-board";
import { useTranslation } from "@/hooks/use-translation";

export default function PipelinePage() {
  const { t } = useTranslation();

  return (
    <div className="flex flex-col gap-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">{t("pipeline.title")}</h1>
        <p className="text-muted-foreground">
          {t("pipeline.description")}
        </p>
      </div>
      <KanbanBoard />
    </div>
  );
}
