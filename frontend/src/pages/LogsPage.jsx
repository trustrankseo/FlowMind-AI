import { useState, useEffect, useCallback } from "react";
import { RefreshCw } from "lucide-react";
import PageHeader from "../components/PageHeader";
import { api } from "../lib/api";

const LEVEL_COLORS = {
  ERROR: "text-danger",
  WARNING: "text-warn",
  INFO: "text-dim",
};

export default function LogsPage() {
  const [logs, setLogs] = useState([]);
  const [auto, setAuto] = useState(true);

  const load = useCallback(async () => {
    try {
      const result = await api.recentLogs(150);
      setLogs(result.logs);
    } catch {
      // stay quiet — logs panel shouldn't be noisy about its own failure
    }
  }, []);

  useEffect(() => {
    load();
    if (!auto) return;
    const interval = setInterval(load, 3000);
    return () => clearInterval(interval);
  }, [load, auto]);

  return (
    <div>
      <PageHeader
        title="Logs"
        description="The last 150 log lines from the running backend."
      />

      <div className="flex items-center gap-4 mb-4">
        <button
          onClick={load}
          className="flex items-center gap-2 text-[12.5px] text-dim hover:text-white"
        >
          <RefreshCw size={13} /> Refresh
        </button>
        <label className="flex items-center gap-2 text-[12.5px] text-dim cursor-pointer">
          <input
            type="checkbox"
            checked={auto}
            onChange={(e) => setAuto(e.target.checked)}
          />
          Auto-refresh every 3s
        </label>
      </div>

      <div className="bg-panel border border-line rounded-xl p-4 font-mono text-[12px] max-h-[70vh] overflow-y-auto space-y-1">
        {logs.length === 0 && <p className="text-dim">No logs yet.</p>}
        {logs.map((log, i) => (
          <div key={i} className="flex gap-3">
            <span className="text-dim shrink-0">{log.time}</span>
            <span className={`shrink-0 ${LEVEL_COLORS[log.level] || "text-dim"}`}>
              {log.level}
            </span>
            <span className="text-white/90 break-all">{log.message}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
