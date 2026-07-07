import { useState } from "react";
import { Globe } from "lucide-react";
import PageHeader from "../components/PageHeader";
import { api } from "../lib/api";

export default function BrowserPage() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function run() {
    if (!url.trim()) return;
    setLoading(true);
    setResult(null);
    try {
      const response = await api.chat("browser-panel", `open browser ${url}`);
      setResult(response.response);
    } catch (err) {
      setResult(`Error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <PageHeader
        title="Browser"
        description="Routes through the Browser Agent via chat — real browser automation isn't wired up yet."
      />

      <div className="bg-warn/10 border border-warn/30 text-warn text-[12.5px] rounded-lg px-3.5 py-2.5 mb-5">
        Heads up: the Browser tool is currently a placeholder in the backend
        (no real page automation yet — see the code review). This panel is wired
        and ready for when that's built.
      </div>

      <div className="flex gap-2 mb-5">
        <div className="flex-1 flex items-center gap-2 bg-panel2 border border-line rounded-full px-4">
          <Globe size={15} className="text-dim shrink-0" />
          <input
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && run()}
            placeholder="https://example.com"
            className="flex-1 bg-transparent py-2.5 text-[13.5px] outline-none"
          />
        </div>
        <button
          onClick={run}
          disabled={loading}
          className="bg-accent text-bg font-medium text-[13px] px-5 rounded-full disabled:opacity-50"
        >
          {loading ? "Running…" : "Open"}
        </button>
      </div>

      {result && (
        <div className="bg-panel border border-line rounded-xl p-4 font-mono text-[12.5px] whitespace-pre-wrap text-dim">
          {result}
        </div>
      )}
    </div>
  );
}
