type Props = {
  prediction?: string;
};

export default function PredictionCard({ prediction }: Props) {
  return (
    <div className="rounded-2xl bg-white p-5 shadow-sm border border-slate-200">
      <h2 className="text-lg font-semibold text-slate-900">Prediction Result</h2>
      <div className="mt-3 rounded-xl bg-indigo-50 p-4">
        <p className="text-sm text-slate-600">Detected class</p>
        <p className="mt-1 text-2xl font-bold text-indigo-700">
          {prediction || "No prediction yet"}
        </p>
      </div>
    </div>
  );
}
