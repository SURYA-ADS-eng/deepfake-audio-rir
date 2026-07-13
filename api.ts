import axios from "axios";
import type { PredictionResponse, AnalysisRecord } from "./types";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
});

export async function uploadAudio(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const { data } = await api.post<PredictionResponse>("/predict", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

  return data;
}

export async function fetchHistory() {
  const { data } = await api.get<AnalysisRecord[]>("/history");
  return data;
}

export default api;
