import { useState, useRef, useEffect } from "react";
import { Send } from "lucide-react";
import PageHeader from "../components/PageHeader";
import { api } from "../lib/api";

const SESSION_ID = "dashboard-session";

export default function ChatPage() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  async function send() {
    const text = input.trim();
    if (!text || loading) return;

    setMessages((prev) => [...prev, { role: "user", text }]);
    setInput("");
    setLoading(true);

    try {
      const result = await api.chat(SESSION_ID, text);
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: result.response },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: `Error: ${err.message}`, error: true },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex flex-col h-full">
      <PageHeader
        title="Chat"
        description="Talk to the Brain — it detects intent and routes to the right agent."
      />

      <div className="flex-1 overflow-y-auto rounded-xl border border-line bg-panel p-4 space-y-4 min-h-0">
        {messages.length === 0 && (
          <p className="text-dim text-[13px] font-mono">
            No messages yet — try "run the tests" or "generate an image of a cat".
          </p>
        )}

        {messages.map((m, i) => (
          <div
            key={i}
            className={`max-w-[85%] ${
              m.role === "user" ? "ml-auto text-right" : ""
            }`}
          >
            <div className="text-[10px] font-mono text-dim mb-1">
              {m.role === "user" ? "YOU" : "FLOWMIND"}
            </div>
            <div
              className={`inline-block text-left px-3.5 py-2.5 rounded-xl text-[13.5px] leading-relaxed whitespace-pre-wrap ${
                m.role === "user"
                  ? "bg-[#2a3f5f] border border-[#3a5580]"
                  : m.error
                  ? "bg-danger/10 border border-danger/30 text-danger"
                  : "bg-panel2 border border-line"
              }`}
            >
              {m.text}
            </div>
          </div>
        ))}

        {loading && (
          <div className="text-dim text-[12px] font-mono">FlowMind is thinking…</div>
        )}

        <div ref={bottomRef} />
      </div>

      <div className="flex gap-2 mt-3">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && send()}
          placeholder="Message FlowMind..."
          className="flex-1 bg-panel2 border border-line rounded-full px-4 py-2.5 text-[13.5px] outline-none focus:border-accent/50"
        />
        <button
          onClick={send}
          disabled={loading}
          className="w-10 h-10 rounded-full bg-accent text-bg flex items-center justify-center disabled:opacity-50 shrink-0"
        >
          <Send size={16} />
        </button>
      </div>
    </div>
  );
}
