import { useState } from "react";
import { Mic } from "lucide-react";
import PageHeader from "../components/PageHeader";
import { api } from "../lib/api";

export default function VoicePage() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function generate() {
    if (!text.trim()) return;
    setLoading(true);
    setResult(null);
    try {
      const response = await api.textToSpeech(text);
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
        title="Voice Agent"
        description="Converts text to spoken audio via Gemini TTS."
      />

      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type what you want FlowMind to say..."
        rows={4}
        className="w-full bg-panel2 border border-line rounded-xl px-4 py-3 text-[13.5px] outline-none focus:border-accent/50 mb-3"
      />

      <button
        onClick={generate}
        disabled={loading}
        className="flex items-center gap-1.5 bg-accent text-bg font-medium text-[13px] px-5 py-2.5 rounded-full disabled:opacity-50 mb-5"
      >
        <Mic size={14} /> {loading ? "Generating…" : "Generate speech"}
      </button>

      {result && !result.success && (
        <div className="bg-danger/10 border border-danger/30 text-danger text-[12.5px] rounded-lg px-3.5 py-2.5">
          {result.error}
        </div>
      )}

      {result?.success && (
        <div className="bg-panel border border-line rounded-xl p-4">
          <audio src={`${api.baseUrl}/${result.audio_path}`} controls className="w-full" />
          <div className="font-mono text-[11px] text-dim mt-2 break-all">
            {result.audio_path}
          </div>
        </div>
      )}
    </div>
  );
}
