import { useState } from "react";
import { Rocket, CheckCircle2, XCircle } from "lucide-react";
import PageHeader from "../components/PageHeader";
import { api } from "../lib/api";

export default function DeploymentPage() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function run() {
    setLoading(true);
    setResult(null);
    try {
      const response = await api.runDeployment();
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
        title="Deployment Agent"
        description="Runs a whitelisted sequence: git pull, then install dependencies. Nothing else."
      />

      <button
        onClick={run}
        disabled={loading}
        className="flex items-center gap-1.5 bg-accent text-bg font-medium text-[13px] px-5 py-2.5 rounded-full disabled:opacity-50 mb-5"
      >
        <Rocket size={14} /> {loading ? "Deploying…" : "Run deployment"}
      </button>

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
            {result.success ? "Deployment succeeded" : result.error || "Deployment failed"}
          </div>

          {result.steps?.map((step, i) => (
            <div key={i} className="bg-panel border border-line rounded-xl overflow-hidden">
              <div className="flex items-center gap-2 px-3.5 py-2 border-b border-line font-mono text-[12px]">
                {step.success ? (
                  <CheckCircle2 size={13} className="text-accent" />
                ) : (
                  <XCircle size={13} className="text-danger" />
                )}
                {step.command}
              </div>
              <pre className="p-3 font-mono text-[11.5px] text-dim overflow-x-auto whitespace-pre-wrap max-h-64">
                {step.output}
              </pre>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
