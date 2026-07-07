import { useState } from "react";
import { FlaskConical, CheckCircle2, XCircle } from "lucide-react";
import PageHeader from "../components/PageHeader";
import { api } from "../lib/api";

export default function TestingPage() {
  const [path, setPath] = useState(".");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function run() {
    setLoading(true);
    setResult(null);
    try {
      const response = await api.runTests(path);
      setResult(response);
    } catch (err) {
      setResult({ success: false, error: err.message });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <PageHeader
        title="Testing Agent"
        description="Runs pytest for real — no mocked results."
      />

      <div className="flex gap-2 mb-5">
        <input
          value={path}
          onChange={(e) => setPath(e.target.value)}
          placeholder="tests"
          className="flex-1 bg-panel2 border border-line rounded-full px-4 py-2.5 text-[13.5px] font-mono outline-none focus:border-accent/50"
        />
        <button
          onClick={run}
          disabled={loading}
          className="flex items-center gap-1.5 bg-accent text-bg font-medium text-[13px] px-5 rounded-full disabled:opacity-50"
        >
          <FlaskConical size={14} /> {loading ? "Running…" : "Run tests"}
        </button>
      </div>

      {result && (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 text-[13.5px] font-medium px-3.5 py-2.5 rounded-lg ${
              result.success
                ? "bg-accentDim text-accent border border-accent/30"
                : "bg-danger/10 text-danger border border-danger/30"
            }`}
          >
            {result.success ? <CheckCircle2 size={16} /> : <XCircle size={16} />}
            {result.summary || result.error}
          </div>

          {result.output && (
            <pre className="bg-panel border border-line rounded-xl p-4 font-mono text-[12px] text-dim overflow-x-auto whitespace-pre-wrap">
              {result.output}
            </pre>
          )}
        </div>
      )}
    </div>
  );
}
