"use client";

import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Building2, MapPin } from "lucide-react";
import { useTranslation } from "@/hooks/use-translation";

// Mock Map for demo when API key is missing
export function CustomerMap() {
  const { t } = useTranslation();
  const [companies, setCompanies] = useState<any[]>([]);
  const [selected, setSelected] = useState<any>(null);

  useEffect(() => {
    fetch("/api/companies")
      .then((res) => res.json())
      .then((data) => setCompanies(data));
  }, []);

  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
      <div className="lg:col-span-3 h-[calc(100vh-12rem)] bg-slate-200 rounded-lg relative overflow-hidden flex flex-col items-center justify-center border-2 border-dashed border-slate-300">
        <MapPin className="h-12 w-12 text-slate-400 mb-4 animate-bounce" />
        <p className="text-slate-500 font-medium">{t("map.interactiveTitle")}</p>
        <p className="text-slate-400 text-sm mt-1">{t("map.apiNotice")}</p>
        
        {/* Mock Markers */}
        <div className="absolute top-1/4 left-1/3 p-2 bg-primary text-white rounded-full shadow-lg cursor-pointer hover:scale-110 transition-transform" onClick={() => setSelected(companies[0])}>
           <Building2 className="h-4 w-4" />
        </div>
        <div className="absolute bottom-1/3 right-1/4 p-2 bg-primary text-white rounded-full shadow-lg cursor-pointer hover:scale-110 transition-transform" onClick={() => setSelected(companies[1])}>
           <Building2 className="h-4 w-4" />
        </div>
      </div>

      <div className="lg:col-span-1 space-y-4">
        <h2 className="font-semibold text-lg">{t("map.customerList")}</h2>
        <div className="space-y-3">
          {companies.map(company => (
            <Card key={company.id} className={`cursor-pointer hover:border-primary transition-colors ${selected?.id === company.id ? 'border-primary bg-primary/5' : ''}`} onClick={() => setSelected(company)}>
              <CardContent className="p-4">
                <div className="font-bold">{company.name}</div>
                <div className="text-xs text-muted-foreground flex items-center gap-1 mt-1">
                  <MapPin className="h-3 w-3" />
                  {company.address}
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
        
        {selected && (
          <div className="mt-6 p-4 bg-white rounded-lg border shadow-sm animate-in fade-in slide-in-from-bottom-2">
            <div className="text-[10px] font-bold text-primary uppercase tracking-wider mb-1">{selected.industry}</div>
            <h3 className="font-bold">{selected.name}</h3>
            <p className="text-xs text-muted-foreground mt-2">{selected.website}</p>
            <button className="w-full mt-4 bg-primary text-white text-sm py-2 rounded-md hover:bg-primary/90 transition-colors">
              {t("map.viewDetails")}
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
