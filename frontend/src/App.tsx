import React, { useState } from "react";
import AudioUploader from "./components/AudioUploader";
import WaveformPlayer from "./components/WaveformPlayer";
import ResultsPanel from "./components/ResultsPanel";
import "./styles.css";

export type AnalysisResult = {
  fake_confidence: number;
  rir_score: number;
  breathing_peaks: number;
  flag: boolean;
};

function App() {
  const [audioFile, setAudioFile] = useState<File | null>(null);
  const [audioUrl, setAudioUrl] = useState<string>("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState("");

  const handleFileSelect = (file: File) => {
    setAudioFile(file);
    setResult(null);
    setError("");
    if (audioUrl) URL.revokeObjectURL(audioUrl);
    setAudioUrl(URL.createObjectURL(file));
  };

  const analyzeAudio = async () => {
    if (!audioFile) return;

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const formData = new FormData();
      formData.append("file", audioFile);

      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Analysis failed");
      }

      const data: AnalysisResult = await response.json();
      setResult(data);
    } catch (err) {
      setError("Unable to analyze audio. Check backend connection.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="hero">
        <h1>AcousticSpace</h1>
        <p>Deepfake detection using room acoustics and breathing patterns</p>
      </header>

      <main className="container">
        <AudioUploader onFileSelect={handleFileSelect} onAnalyze={analyzeAudio} loading={loading} />

        {audioUrl && (
          <section className="card">
            <h2>Waveform Preview</h2>
            <WaveformPlayer audioUrl={audioUrl} />
          </section>
        )}

        {error && <div className="error-box">{error}</div>}

        {result && <ResultsPanel result={result} />}
      </main>
    </div>
  );
}

export default App;
