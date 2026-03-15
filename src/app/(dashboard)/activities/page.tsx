"use client";

import { useTranslation } from "@/hooks/use-translation";

export default function ActivitiesPage() {
  const { t } = useTranslation();

  return (
    <div className="flex flex-col gap-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">{t("activities.title")}</h1>
        <p className="text-muted-foreground">
          {t("activities.description")}
        </p>
      </div>
      <div className="h-96 flex items-center justify-center border-2 border-dashed rounded-lg text-muted-foreground">
        Activities Log implementation coming soon...
      </div>
    </div>
  );
}
