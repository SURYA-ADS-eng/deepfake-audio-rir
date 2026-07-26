import React, { useEffect, useRef } from "react";

type Props = {
  audioUrl: string;
};

function WaveformPlayer({ audioUrl }: Props) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const audioContextRef = useRef<AudioContext | null>(null);

  useEffect(() => {
    const analyzeAudio = async () => {
      try {
        const response = await fetch(audioUrl);
        const arrayBuffer = await response.arrayBuffer();

        const audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
        audioContextRef.current = audioContext;

        const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);
        drawWaveform(audioBuffer);
      } catch (error) {
        console.error("Error loading audio:", error);
      }
    };

    analyzeAudio();
  }, [audioUrl]);

  const drawWaveform = (audioBuffer: AudioBuffer) => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const data = audioBuffer.getChannelData(0);
    const width = canvas.width;
    const height = canvas.height;

    ctx.fillStyle = "#1a1a1a";
    ctx.fillRect(0, 0, width, height);

    ctx.strokeStyle = "#4a9eff";
    ctx.lineWidth = 2;
    ctx.beginPath();

    const step = Math.ceil(data.length / width);
    const amp = height / 2;

    for (let i = 0; i < width; i++) {
      let min = 1.0;
      let max = -1.0;

      for (let j = 0; j < step; j++) {
        const datum = data[i * step + j];
        if (datum < min) min = datum;
        if (datum > max) max = datum;
      }

      const x = i;
      const y1 = amp - max * amp;
      const y2 = amp - min * amp;

      if (i === 0) {
        ctx.moveTo(x, y1);
      } else {
        ctx.lineTo(x, y1);
        ctx.lineTo(x, y2);
      }
    }

    ctx.stroke();
  };

  return (
    <canvas
      ref={canvasRef}
      width={600}
      height={150}
      style={{ width: "100%", backgroundColor: "#1a1a1a", borderRadius: "4px" }}
    />
  );
}

export default WaveformPlayer;
