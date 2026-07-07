import { useState } from "react";
import { Clapperboard } from "lucide-react";
import PageHeader from "../components/PageHeader";
import { api } from "../lib/api";

export default function VideoPage() {
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function generate() {
    if (!prompt.trim()) return;
    setLoading(true);
    setResult(null);
    try {
      const response = await api.generateVideo(prompt);
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
        title="Video Agent"
        description="Generates short videos from a text prompt via Gemini/Veo. This can take a couple of minutes — the request waits for it to finish."
      />

      <div className="flex gap-2 mb-5">
        <input
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && generate()}
          placeholder="a golden retriever puppy running through a field"
          className="flex-1 bg-panel2 border border-line rounded-full px-4 py-2.5 text-[13.5px] outline-none focus:border-accent/50"
        />
        <button
          onClick={generate}
          disabled={loading}
          className="flex items-center gap-1.5 bg-accent text-bg font-medium text-[13px] px-5 rounded-full disabled:opacity-50"
        >
          <Clapperboard size={14} /> {loading ? "Generating…" : "Generate"}
        </button>
      </div>

      {loading && (
        <p className="text-dim text-[12.5px] font-mono mb-4">
          Waiting on Veo — this can take a minute or two…
        </p>
      )}

      {result && !result.success && (
        <div className="bg-danger/10 border border-danger/30 text-danger text-[12.5px] rounded-lg px-3.5 py-2.5">
          {result.error}
        </div>
      )}

      {result?.success && (
        <div className="space-y-3">
          {result.videos.map((path) => (
            <div key={path} className="bg-panel border border-line rounded-xl overflow-hidden">
              <video src={`${api.baseUrl}/${path}`} controls className="w-full max-h-96" />
              <div className="font-mono text-[11px] text-dim p-2 break-all">{path}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
