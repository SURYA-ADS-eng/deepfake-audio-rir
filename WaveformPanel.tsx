import { useEffect, useRef } from "react";
import WaveSurfer from "wavesurfer.js";
import Spectrogram from "wavesurfer.js/dist/plugins/spectrogram.esm.js";

type Props = {
  audioUrl?: string;
  spectrogramUrl?: string;
};

export default function WaveformPanel({ audioUrl }: Props) {
  const waveformRef = useRef<HTMLDivElement | null>(null);
  const spectrogramRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!waveformRef.current || !audioUrl) return;

    const ws = WaveSurfer.create({
      container: waveformRef.current,
      waveColor: "#6366f1",
      progressColor: "#1e1b4b",
      height: 120,
      barWidth: 2,
      barGap: 1,
      normalize: true,
    });

    ws.load(audioUrl);

    const plugin = ws.registerPlugin(
      Spectrogram.create({
        container: spectrogramRef.current as HTMLElement,
        labels: true,
      })
    );

    return () => {
      plugin.destroy();
      ws.destroy();
    };
  }, [audioUrl]);

  return (
    <div className="rounded-2xl bg-white p-5 shadow-sm border border-slate-200">
      <h2 className="text-lg font-semibold text-slate-900">Audio Visualization</h2>
      <div className="mt-4 rounded-xl bg-slate-50 p-3">
        <div ref={waveformRef} />
      </div>
      <div className="mt-4">
        <p className="mb-2 text-sm font-medium text-slate-700">Spectrogram</p>
        <div ref={spectrogramRef} className="rounded-xl bg-slate-50 p-3 overflow-hidden" />
      </div>
    </div>
  );
}
