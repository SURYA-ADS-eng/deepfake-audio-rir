import AudioUploader from "../components/AudioUploader";
import WaveformPanel from "../components/WaveformPanel";
import PredictionCard from "../components/PredictionCard";
import ConfidenceGauge from "../components/ConfidenceGauge";
import SuspiciousRegions from "../components/SuspiciousRegions";
import HistoryPanel from "../components/HistoryPanel";
import type { AnalysisRecord, PredictionResponse } from "../types";

type Props = {
  onUpload: (file: File) => void;
  loading: boolean;
  result: PredictionResponse | null;
  history: AnalysisRecord[];
};

export default function Dashboard({ onUpload, loading, result, history }: Props) {
  return (
    <div className="grid gap-4">
      <AudioUploader onUpload={onUpload} loading={loading} />

      <div className="grid gap-4 lg:grid-cols-2">
        <PredictionCard prediction={result?.prediction} />
        <ConfidenceGauge value={(result?.confidence || 0) * 100 <= 100 ? (result?.confidence || 0) : (result?.confidence || 0)} />
      </div>

      <div className="grid gap-4 lg:grid-cols-2">
        <WaveformPanel audioUrl={result?.waveform_url} />
        <SuspiciousRegions regions={result?.suspicious_regions || []} />
      </div>

      <HistoryPanel items={history} />
    </div>
  );
}
