import type { AnalysisRecord } from "../types";

type Props = {
  items: AnalysisRecord[];
};

export default function HistoryPanel({ items }: Props) {
  return (
    <div className="rounded-2xl bg-white p-5 shadow-sm border border-slate-200">
      <h2 className="text-lg font-semibold text-slate-900">Analysis History</h2>
      <div className="mt-4 overflow-x-auto">
        <table className="min-w-full text-sm">
          <thead>
            <tr className="text-left text-slate-500">
              <th className="py-2">File</th>
              <th className="py-2">Prediction</th>
              <th className="py-2">Confidence</th>
              <th className="py-2">Suspicious</th>
              <th className="py-2">Time</th>
            </tr>
          </thead>
          <tbody>
            {items.map((row) => (
              <tr key={row.id} className="border-t border-slate-100">
                <td className="py-3 text-slate-700">{row.file_name}</td>
                <td className="py-3">{row.prediction}</td>
                <td className="py-3">{row.confidence}%</td>
                <td className="py-3">{row.suspicious_count}</td>
                <td className="py-3 text-slate-600">{row.created_at}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
