type Props = {
  value: number;
};

export default function ConfidenceGauge({ value }: Props) {
  const clamped = Math.max(0, Math.min(100, value));
  const strokeDashoffset = 283 - (283 * clamped) / 100;

  return (
    <div className="rounded-2xl bg-white p-5 shadow-sm border border-slate-200">
      <h2 className="text-lg font-semibold text-slate-900">Confidence</h2>
      <div className="mt-4 flex items-center justify-center">
        <div className="relative h-40 w-40">
          <svg viewBox="0 0 100 100" className="h-40 w-40 -rotate-90">
            <circle cx="50" cy="50" r="45" stroke="#e2e8f0" strokeWidth="10" fill="none" />
            <circle
              cx="50"
              cy="50"
              r="45"
              stroke="#4f46e5"
              strokeWidth="10"
              fill="none"
              strokeDasharray="283"
              strokeDashoffset={strokeDashoffset}
              strokeLinecap="round"
            />
          </svg>
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="text-center">
              <div className="text-3xl font-bold text-slate-900">{clamped.toFixed(0)}%</div>
              <div className="text-xs text-slate-500">Model confidence</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
