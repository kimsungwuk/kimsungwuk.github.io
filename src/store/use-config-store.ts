import { create } from "zustand";
import { persist } from "zustand/middleware";

type Language = "ko" | "en";

interface ConfigState {
  language: Language;
  setLanguage: (lang: Language) => void;
}

export const useConfigStore = create<ConfigState>()(
  persist(
    (set) => ({
      language: "ko",
      setLanguage: (lang) => set({ language: lang }),
    }),
    {
      name: "finder-config",
    }
  )
);
