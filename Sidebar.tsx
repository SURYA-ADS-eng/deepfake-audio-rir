type Props = {
  active: string;
  setActive: (v: string) => void;
};

const tabs = ["dashboard", "results", "history"];

export default function Sidebar({ active, setActive }: Props) {
  return (
    <aside className="w-full border-b border-slate-200 bg-white px-4 py-3 md:h-screen md:w-64 md:border-b-0 md:border-r">
      <div className="text-xl font-bold text-slate-900">AudioShield</div>
      <nav className="mt-4 flex gap-2 md:flex-col">
        {tabs.map((tab) => (
          <button
            key={tab}
            onClick={() => setActive(tab)}
            className={`rounded-xl px-4 py-2 text-left capitalize ${
              active === tab ? "bg-indigo-600 text-white" : "bg-slate-100 text-slate-700"
            }`}
          >
            {tab}
          </button>
        ))}
      </nav>
    </aside>
  );
}
