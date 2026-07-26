import React from "react";

type Props = {
  onFileSelect: (file: File) => void;
  onAnalyze: () => void;
  loading: boolean;
};

function AudioUploader({ onFileSelect, onAnalyze, loading }: Props) {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) onFileSelect(file);
  };

  return (
    <section className="card">
      <h2>Upload Audio</h2>
      <input
        type="file"
        accept="audio/*"
        onChange={handleChange}
        className="file-input"
      />
      <button className="primary-btn" onClick={onAnalyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Audio"}
      </button>
    </section>
  );
}

export default AudioUploader;
