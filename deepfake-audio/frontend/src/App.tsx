import { useState } from 'react';

interface AnalysisResult {
  predicted_label: string;
  confidence: number;
  rir_features: Record<string, number>;
  breath_features: Record<string, number>;
  spectrogram_shape: [number, number];
}

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setResult(null);
    setError(null);
    const selectedFile = event.target.files?.[0] ?? null;
    setFile(selectedFile);
  };

  const uploadAudio = async () => {
    if (!file) return;
    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('API request failed');
      }

      const json = (await response.json()) as AnalysisResult;
      setResult(json);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <header>
        <h1>AcousticSpace</h1>
        <p>Deepfake audio detection with Room Impulse Response analysis.</p>
      </header>

      <section className="upload-panel">
        <label htmlFor="audio-upload">Upload audio file</label>
        <input id="audio-upload" type="file" accept="audio/*" onChange={handleFileChange} />
        <button onClick={uploadAudio} disabled={!file || loading}>
          {loading ? 'Analyzing...' : 'Analyze Audio'}
        </button>
        {error && <p className="error">{error}</p>}
      </section>

      <section className="result-panel">
        {result ? (
          <div>
            <h2>Analysis Result</h2>
            <p>
              Predicted label: <strong>{result.predicted_label}</strong>
            </p>
            <p>
              Confidence: <strong>{(result.confidence * 100).toFixed(1)}%</strong>
            </p>
            <div className="feature-grid">
              <div>
                <h3>RIR</h3>
                <pre>{JSON.stringify(result.rir_features, null, 2)}</pre>
              </div>
              <div>
                <h3>Breathing</h3>
                <pre>{JSON.stringify(result.breath_features, null, 2)}</pre>
              </div>
            </div>
            <p>Spectrogram shape: {result.spectrogram_shape.join(' x ')}</p>
          </div>
        ) : (
          <p>Upload an audio file and press Analyze to inspect the recording.</p>
        )}
      </section>
    </div>
  );
}

export default App;
