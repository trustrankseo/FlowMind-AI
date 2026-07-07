import { useState, useEffect } from "react";
import { RefreshCw } from "lucide-react";
import PageHeader from "../components/PageHeader";
import { api } from "../lib/api";

export default function GitHubPage() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  async function load() {
    setLoading(true);
    setError(null);
    try {
      const result = await api.githubSummary();
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load();
  }, []);

  return (
    <div>
      <PageHeader
        title="GitHub"
        description="A live summary of the connected repository."
      />

      <button
        onClick={load}
        className="flex items-center gap-2 text-[12.5px] text-dim hover:text-white mb-4"
      >
        <RefreshCw size={13} className={loading ? "animate-spin" : ""} />
        Refresh
      </button>

      {error && (
        <div className="bg-danger/10 border border-danger/30 text-danger text-[12.5px] rounded-lg px-3.5 py-2.5">
          {error}
        </div>
      )}

      {data && (
        <pre className="bg-panel border border-line rounded-xl p-4 font-mono text-[12.5px] text-dim overflow-x-auto">
          {JSON.stringify(data, null, 2)}
        </pre>
      )}
    </div>
  );
}
