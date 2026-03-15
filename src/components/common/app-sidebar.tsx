"use client";

import {
  LayoutDashboard,
  Building2,
  Kanban,
  Calendar,
  Settings,
  Map,
  Search,
  Globe,
} from "lucide-react";

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarGroup,
  SidebarGroupLabel,
  SidebarGroupContent,
} from "@/components/ui/sidebar";
import Link from "next/link";
import { useTranslation } from "@/hooks/use-translation";
import { useConfigStore } from "@/store/use-config-store";
import { Button } from "@/components/ui/button";

export function AppSidebar() {
  const { t, language } = useTranslation();
  const { setLanguage } = useConfigStore();

  const items = [
    {
      title: t("common.dashboard"),
      url: "/dashboard",
      icon: LayoutDashboard,
    },
    {
      title: t("common.pipeline"),
      url: "/pipeline",
      icon: Kanban,
    },
    {
      title: t("common.companies"),
      url: "/companies",
      icon: Building2,
    },
    {
      title: t("common.activities"),
      url: "/activities",
      icon: Calendar,
    },
    {
      title: t("common.mapExplorer"),
      url: "/map",
      icon: Map,
    },
    {
      title: t("common.ocrScan"),
      url: "/ocr",
      icon: Search,
    },
  ];

  return (
    <Sidebar>
      <SidebarHeader className="p-4 border-b">
        <div className="flex items-center justify-between gap-2">
          <div className="flex items-center gap-2 font-bold text-xl">
            <div className="bg-primary text-primary-foreground p-1 rounded">F</div>
            <span>Finder CRM</span>
          </div>
          <Button 
            variant="ghost" 
            size="icon" 
            className="h-8 w-8"
            onClick={() => setLanguage(language === "ko" ? "en" : "ko")}
            title="Switch Language"
          >
            <Globe className="h-4 w-4" />
          </Button>
        </div>
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Menu</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild>
                    <Link href={item.url}>
                      <item.icon className="h-4 w-4" />
                      <span>{item.title}</span>
                    </Link>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter className="p-4 border-t">
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton asChild>
              <Link href="/settings">
                <Settings className="h-4 w-4" />
                <span>{t("common.settings")}</span>
              </Link>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarFooter>
    </Sidebar>
  );
}
