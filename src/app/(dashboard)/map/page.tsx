"use client";

import { CustomerMap } from "@/components/map/customer-map";
import { useTranslation } from "@/hooks/use-translation";

export default function MapPage() {
  const { t } = useTranslation();

  return (
    <div className="flex flex-col gap-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">{t("map.title")}</h1>
          <p className="text-muted-foreground">
            {t("map.description")}
          </p>
        </div>
      </div>
      <CustomerMap />
    </div>
  );
}
