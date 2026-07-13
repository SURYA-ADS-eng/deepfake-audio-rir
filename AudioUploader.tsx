import { useState } from "react";

type Props = {
  onUpload: (file: File) => void;
  loading?: boolean;
};

export default function AudioUploader({ onUpload, loading }: Props) {
  const [file, setFile] = useState<File | null>(null);

  return (
    <div className="rounded-2xl bg-white p-5 shadow-sm border border-slate-200">
      <h2 className="text-lg font-semibold text-slate-900">Upload Audio</h2>
      <p className="mt-1 text-sm text-slate-500">MP3, WAV, or M4A supported.</p>

      <div className="mt-4">
        <input
          type="file"
          accept=".mp3,.wav,.m4a,audio/*"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          className="block w-full text-sm text-slate-700 file:mr-4 file:rounded-xl file:border-0 file:bg-indigo-600 file:px-4 file:py-2 file:text-white hover:file:bg-indigo-700"
        />
      </div>

      <button
        disabled={!file || loading}
        onClick={() => file && onUpload(file)}
        className="mt-4 rounded-xl bg-slate-900 px-4 py-2 text-white disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading ? "Analyzing..." : "Upload & Analyze"}
      </button>
    </div>
  );
}
