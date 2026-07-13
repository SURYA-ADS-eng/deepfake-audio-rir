export type PredictionResponse = {
  file_name: string;
  prediction: string;
  confidence: number;
  suspicious_regions: { start: number; end: number; label?: string }[];
  waveform_url?: string;
  spectrogram_url?: string;
  created_at?: string;
};

export type AnalysisRecord = {
  id: string;
  file_name: string;
  prediction: string;
  confidence: number;
  created_at: string;
  suspicious_count: number;
};
