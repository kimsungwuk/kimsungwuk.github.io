"use client";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { 
  Building2, 
  Users, 
  TrendingUp, 
  CheckCircle2,
  ArrowUpRight,
  ArrowDownRight,
  Loader2
} from "lucide-react";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { useTranslation } from "@/hooks/use-translation";

export default function DashboardPage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const { t } = useTranslation();
  const [stats, setStats] = useState<any>(null);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    if (status === "unauthenticated") {
      router.push("/login");
    } else if (status === "authenticated") {
      fetch("/api/deals")
        .then(res => res.json())
        .then(data => {
            setStats({
                companies: 2,
                deals: Array.isArray(data) ? data.length : 0,
                revenue: Array.isArray(data) ? data.reduce((acc: number, d: any) => acc + d.value, 0) : 0
            });
        });
    }
  }, [status, router]);

  if (!mounted || status === "loading" || !stats) {
    return (
        <div className="flex h-96 items-center justify-center">
            <Loader2 className="h-8 w-8 animate-spin text-primary" />
        </div>
    );
  }

  const cards = [
    {
      title: t("dashboard.totalCompanies"),
      value: stats.companies,
      icon: Building2,
      trend: "+12% " + t("dashboard.trendLastMonth"),
      trendType: "up"
    },
    {
      title: t("dashboard.activeDeals"),
      value: stats.deals,
      icon: TrendingUp,
      trend: "+5% " + t("dashboard.trendLastMonth"),
      trendType: "up"
    },
    {
      title: t("dashboard.pipelineValue"),
      value: "$" + stats.revenue.toLocaleString(),
      icon: CheckCircle2,
      trend: "-2% " + t("dashboard.trendLastMonth"),
      trendType: "down"
    },
    {
      title: t("dashboard.conversionRate"),
      value: "24.5%",
      icon: Users,
      trend: "+4% " + t("dashboard.trendLastMonth"),
      trendType: "up"
    }
  ];

  return (
    <div className="flex flex-col gap-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">{t("common.dashboard")}</h1>
        <p className="text-muted-foreground">
          {t("common.welcome")}, {session?.user?.name}! {t("common.overview")}
        </p>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {cards.map((card) => (
          <Card key={card.title}>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">
                {card.title}
              </CardTitle>
              <card.icon className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{card.value}</div>
              <p className="text-xs text-muted-foreground flex items-center gap-1 mt-1">
                {card.trendType === "up" ? (
                  <ArrowUpRight className="h-3 w-3 text-emerald-500" />
                ) : (
                  <ArrowDownRight className="h-3 w-3 text-rose-500" />
                )}
                {card.trend}
              </p>
            </CardContent>
          </Card>
        ))}
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
        <Card className="col-span-4">
          <CardHeader>
            <CardTitle>{t("dashboard.recentActivity")}</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-[200px] flex flex-col items-center justify-center text-muted-foreground border-2 border-dashed rounded-lg">
              <p>{t("dashboard.activityNotice")}</p>
              <p className="text-xs">({t("dashboard.demoData")})</p>
            </div>
          </CardContent>
        </Card>
        <Card className="col-span-3">
          <CardHeader>
            <CardTitle>{t("dashboard.recentCompanies")}</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-[200px] flex flex-col items-center justify-center text-muted-foreground border-2 border-dashed rounded-lg">
              <p>{t("dashboard.companyNotice")}</p>
              <p className="text-xs">({t("dashboard.demoData")})</p>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
