import React from "react";
import type { AnalysisResult } from "../app";

type Props = {
  result: AnalysisResult;
};

function ResultsPanel({ result }: Props) {
  const confidence = Math.round(result.fake_confidence * 100);

  return (
    <section className="card results">
      <h2>Analysis Results</h2>

      <div className="metric-grid">
        <div className="metric">
          <span className="label">Fake Confidence</span>
          <span className="value">{confidence}%</span>
        </div>

        <div className="metric">
          <span className="label">RIR Score</span>
          <span className="value">{result.rir_score.toFixed(3)}</span>
        </div>

        <div className="metric">
          <span className="label">Breathing Peaks</span>
          <span className="value">{result.breathing_peaks}</span>
        </div>
      </div>

      <div className={`flag-banner ${result.flag ? "flagged" : "safe"}`}>
        {result.flag ? "Suspicious audio detected" : "No strong deepfake signal detected"}
      </div>
    </section>
  );
}

export default ResultsPanel;
