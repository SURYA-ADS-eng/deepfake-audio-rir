type Region = { start: number; end: number; label?: string };

type Props = {
  regions: Region[];
};

export default function SuspiciousRegions({ regions }: Props) {
  return (
    <div className="rounded-2xl bg-white p-5 shadow-sm border border-slate-200">
      <h2 className="text-lg font-semibold text-slate-900">Suspicious Regions</h2>
      <div className="mt-4 space-y-3">
        {regions.length === 0 ? (
          <p className="text-sm text-slate-500">No suspicious segments detected.</p>
        ) : (
          regions.map((r, i) => (
            <div key={i} className="flex items-center justify-between rounded-xl bg-rose-50 px-4 py-3">
              <div>
                <p className="font-medium text-rose-700">
                  {r.label || `Region ${i + 1}`}
                </p>
                <p className="text-sm text-slate-600">
                  {r.start.toFixed(2)}s - {r.end.toFixed(2)}s
                </p>
              </div>
              <span className="rounded-full bg-rose-100 px-3 py-1 text-xs font-semibold text-rose-700">
                Flagged
              </span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
