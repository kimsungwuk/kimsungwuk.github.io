"use client";

import { BusinessCardOCR } from "@/components/forms/business-card-ocr";
import { useTranslation } from "@/hooks/use-translation";

export default function OCRPage() {
  const { t } = useTranslation();

  return (
    <div className="flex flex-col gap-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">{t("ocr.title")}</h1>
        <p className="text-muted-foreground">
          {t("ocr.description")}
        </p>
      </div>
      <BusinessCardOCR />
    </div>
  );
}
