"use client";

import React, { useState, useRef } from "react";
import Tesseract from "tesseract.js";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Camera, Upload, Loader2, RefreshCw, UserPlus } from "lucide-react";
import { useTranslation } from "@/hooks/use-translation";

export function BusinessCardOCR() {
  const { t } = useTranslation();
  const [image, setImage] = useState<string | null>(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [progress, setProgress] = useState(0);
  const [results, setResults] = useState({
    name: "",
    title: "",
    phone: "",
    email: "",
    company: "",
  });

  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        setImage(reader.result as string);
        processImage(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  const processImage = async (imageSrc: string) => {
    setIsProcessing(true);
    setProgress(0);
    try {
      const result = await Tesseract.recognize(imageSrc, "eng+kor", {
        logger: (m) => {
          if (m.status === "recognizing text") {
            setProgress(Math.round(m.progress * 100));
          }
        },
      });

      const text = result.data.text;
      console.log("Extracted Text:", text);
      parseText(text);
    } catch (error) {
      console.error("OCR Error:", error);
    } finally {
      setIsProcessing(false);
    }
  };

  const parseText = (text: string) => {
    const lines = text.split("\n").filter((line) => line.trim().length > 0);
    
    // Simple heuristic-based parsing
    const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;
    const phoneRegex = /(\d{2,3}[-.\s]??\d{3,4}[-.\s]??\d{4})/;

    const emailMatch = text.match(emailRegex);
    const phoneMatch = text.match(phoneRegex);

    setResults({
      name: lines[0] || "",
      title: lines[1] || "",
      email: emailMatch ? emailMatch[0] : "",
      phone: phoneMatch ? phoneMatch[0] : "",
      company: lines[lines.length - 1] || "",
    });
  };

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <Card>
        <CardHeader>
          <CardTitle>{t("ocr.uploadTitle")}</CardTitle>
          <CardDescription>
            {t("ocr.uploadDesc")}
          </CardDescription>
        </CardHeader>
        <CardContent className="flex flex-col items-center gap-6">
          <div 
            className="w-full aspect-[1.6/1] border-2 border-dashed rounded-xl flex flex-col items-center justify-center bg-slate-50 dark:bg-slate-900 overflow-hidden relative"
          >
            {image ? (
              <img src={image} alt="Business Card" className="w-full h-full object-contain" />
            ) : (
              <div className="flex flex-col items-center text-muted-foreground">
                <Camera className="h-12 w-12 mb-2 opacity-20" />
                <p>{t("common.noImage")}</p>
              </div>
            )}
            
            {isProcessing && (
              <div className="absolute inset-0 bg-background/60 backdrop-blur-sm flex flex-col items-center justify-center">
                <Loader2 className="h-10 w-10 animate-spin text-primary mb-2" />
                <p className="font-medium">{t("common.processing")} {progress}%</p>
              </div>
            )}
          </div>

          <div className="flex gap-4 w-full">
            <Button 
              className="flex-1" 
              onClick={() => fileInputRef.current?.click()}
              disabled={isProcessing}
            >
              <Upload className="h-4 w-4 mr-2" />
              {t("common.upload")}
            </Button>
            <input 
              type="file" 
              ref={fileInputRef} 
              className="hidden" 
              accept="image/*" 
              onChange={handleImageUpload}
            />
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>{t("ocr.resultTitle")}</CardTitle>
          <CardDescription>
            {t("ocr.resultDesc")}
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="name">{t("ocr.fields.name")}</Label>
            <Input 
              id="name" 
              value={results.name} 
              onChange={(e) => setResults({ ...results, name: e.target.value })} 
            />
          </div>
          <div className="space-y-2">
            <Label htmlFor="title">{t("ocr.fields.title")}</Label>
            <Input 
              id="title" 
              value={results.title} 
              onChange={(e) => setResults({ ...results, title: e.target.value })} 
            />
          </div>
          <div className="space-y-2">
            <Label htmlFor="company">{t("ocr.fields.company")}</Label>
            <Input 
              id="company" 
              value={results.company} 
              onChange={(e) => setResults({ ...results, company: e.target.value })} 
            />
          </div>
          <div className="space-y-2">
            <Label htmlFor="email">{t("ocr.fields.email")}</Label>
            <Input 
              id="email" 
              value={results.email} 
              onChange={(e) => setResults({ ...results, email: e.target.value })} 
            />
          </div>
          <div className="space-y-2">
            <Label htmlFor="phone">{t("ocr.fields.phone")}</Label>
            <Input 
              id="phone" 
              value={results.phone} 
              onChange={(e) => setResults({ ...results, phone: e.target.value })} 
            />
          </div>

          <div className="pt-4 flex gap-4">
            <Button variant="outline" className="flex-1" onClick={() => setImage(null)}>
              <RefreshCw className="h-4 w-4 mr-2" />
              {t("common.reset")}
            </Button>
            <Button className="flex-1">
              <UserPlus className="h-4 w-4 mr-2" />
              {t("ocr.addToContacts")}
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
