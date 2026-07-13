import { useEffect, useState } from "react";
import Sidebar from "./components/Sidebar";
import Dashboard from "./pages/Dashboard";
import { fetchHistory, uploadAudio } from "./api";
import type { AnalysisRecord, PredictionResponse } from "./types";

export default function App() {
  const [active, setActive] = useState("dashboard");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PredictionResponse | null>(null);
  const [history, setHistory] = useState<AnalysisRecord[]>([]);

  useEffect(() => {
    fetchHistory().then(setHistory).catch(() => {});
  }, []);

  const handleUpload = async (file: File) => {
    setLoading(true);
    try {
      const data = await uploadAudio(file);
      setResult(data);
      setHistory((prev) => [
        {
          id: crypto.randomUUID(),
          file_name: data.file_name,
          prediction: data.prediction,
          confidence: data.confidence,
          created_at: data.created_at || new Date().toISOString(),
          suspicious_count: data.suspicious_regions?.length || 0,
        },
        ...prev,
      ]);
      setActive("results");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 md:flex">
      <Sidebar active={active} setActive={setActive} />
      <main className="flex-1 p-4 md:p-6">
        {active === "dashboard" || active === "results" ? (
          <Dashboard onUpload={handleUpload} loading={loading} result={result} history={history} />
        ) : (
          <Dashboard onUpload={handleUpload} loading={loading} result={result} history={history} />
        )}
      </main>
    </div>
  );
}
