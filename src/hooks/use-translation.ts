import en from "@/locales/en.json";
import ko from "@/locales/ko.json";
import { useConfigStore } from "@/store/use-config-store";

export const useTranslation = () => {
  const { language } = useConfigStore();
  const translations = language === "ko" ? ko : en;

  const t = (path: string) => {
    return path.split(".").reduce((obj: any, key) => obj?.[key], translations) || path;
  };

  return { t, language };
};
