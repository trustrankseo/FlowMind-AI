import { useState } from "react";
import { Sparkles } from "lucide-react";
import PageHeader from "../components/PageHeader";
import { api } from "../lib/api";

export default function ImagePage() {
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function generate() {
    if (!prompt.trim()) return;
    setLoading(true);
    setResult(null);
    try {
      const response = await api.generateImage(prompt);
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
        title="Image Agent"
        description="Generates images from a text prompt via Gemini/Imagen."
      />

      <div className="flex gap-2 mb-5">
        <input
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && generate()}
          placeholder="a cat on a rooftop at sunset, cinematic"
          className="flex-1 bg-panel2 border border-line rounded-full px-4 py-2.5 text-[13.5px] outline-none focus:border-accent/50"
        />
        <button
          onClick={generate}
          disabled={loading}
          className="flex items-center gap-1.5 bg-accent text-bg font-medium text-[13px] px-5 rounded-full disabled:opacity-50"
        >
          <Sparkles size={14} /> {loading ? "Generating…" : "Generate"}
        </button>
      </div>

      {result && !result.success && (
        <div className="bg-danger/10 border border-danger/30 text-danger text-[12.5px] rounded-lg px-3.5 py-2.5">
          {result.error}
        </div>
      )}

      {result?.success && (
        <div className="grid grid-cols-2 gap-3">
          {result.images.map((path) => (
            <div key={path} className="bg-panel border border-line rounded-xl overflow-hidden">
              <img
                src={`${api.baseUrl}/${path}`}
                alt={prompt}
                className="w-full h-48 object-cover"
              />
              <div className="font-mono text-[11px] text-dim p-2 break-all">{path}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
