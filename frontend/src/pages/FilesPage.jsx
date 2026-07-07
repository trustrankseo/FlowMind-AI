import { useState, useEffect, useCallback } from "react";
import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import { javascript } from "@codemirror/lang-javascript";
import { oneDark } from "@codemirror/theme-one-dark";
import { Folder, File as FileIcon, Save, RefreshCw } from "lucide-react";
import PageHeader from "../components/PageHeader";
import { api } from "../lib/api";

function languageFor(path) {
  if (path.endsWith(".py")) return [python()];
  if (path.endsWith(".js") || path.endsWith(".jsx")) return [javascript({ jsx: true })];
  return [];
}

export default function FilesPage() {
  const [currentDir, setCurrentDir] = useState(".");
  const [entries, setEntries] = useState([]);
  const [selectedPath, setSelectedPath] = useState(null);
  const [content, setContent] = useState("");
  const [status, setStatus] = useState("");
  const [loadingList, setLoadingList] = useState(false);

  const loadDir = useCallback(async (path) => {
    setLoadingList(true);
    try {
      const result = await api.listFiles(path);
      setCurrentDir(result.path);
      setEntries(result.entries);
    } catch (err) {
      setStatus(`Error: ${err.message}`);
    } finally {
      setLoadingList(false);
    }
  }, []);

  useEffect(() => {
    loadDir(".");
  }, [loadDir]);

  async function openEntry(entry) {
    if (entry.is_dir) {
      loadDir(entry.path);
      return;
    }
    try {
      const result = await api.readFile(entry.path);
      setSelectedPath(entry.path);
      setContent(result.content);
      setStatus("");
    } catch (err) {
      setStatus(`Error: ${err.message}`);
    }
  }

  async function save() {
    if (!selectedPath) return;
    try {
      await api.saveFile(selectedPath, content);
      setStatus("Saved.");
    } catch (err) {
      setStatus(`Error: ${err.message}`);
    }
  }

  function goUp() {
    if (currentDir === ".") return;
    const parts = currentDir.split("/");
    parts.pop();
    loadDir(parts.length ? parts.join("/") : ".");
  }

  return (
    <div className="flex flex-col h-full">
      <PageHeader
        title="Files & Editor"
        description="Browse the project and edit files directly — confined to the project directory."
      />

      <div className="flex-1 flex gap-4 min-h-0">
        {/* Explorer */}
        <div className="w-64 shrink-0 bg-panel border border-line rounded-xl flex flex-col min-h-0">
          <div className="flex items-center justify-between px-3 py-2 border-b border-line">
            <span className="font-mono text-[11px] text-dim truncate">/{currentDir}</span>
            <button onClick={() => loadDir(currentDir)} className="text-dim hover:text-white">
              <RefreshCw size={13} className={loadingList ? "animate-spin" : ""} />
            </button>
          </div>
          <div className="flex-1 overflow-y-auto p-1.5">
            {currentDir !== "." && (
              <button
                onClick={goUp}
                className="w-full text-left px-2.5 py-1.5 rounded-lg text-[13px] text-dim hover:bg-panel2 flex items-center gap-2"
              >
                <Folder size={14} /> ..
              </button>
            )}
            {entries.map((entry) => (
              <button
                key={entry.path}
                onClick={() => openEntry(entry)}
                className={`w-full text-left px-2.5 py-1.5 rounded-lg text-[13px] flex items-center gap-2 hover:bg-panel2 ${
                  selectedPath === entry.path ? "bg-accentDim text-accent" : ""
                }`}
              >
                {entry.is_dir ? (
                  <Folder size={14} className="shrink-0" />
                ) : (
                  <FileIcon size={14} className="shrink-0" />
                )}
                <span className="truncate">{entry.name}</span>
              </button>
            ))}
          </div>
        </div>

        {/* Editor */}
        <div className="flex-1 bg-panel border border-line rounded-xl flex flex-col min-h-0 overflow-hidden">
          <div className="flex items-center justify-between px-4 py-2 border-b border-line">
            <span className="font-mono text-[12px] text-dim truncate">
              {selectedPath || "No file open"}
            </span>
            <div className="flex items-center gap-3">
              {status && <span className="text-[11px] text-dim">{status}</span>}
              <button
                onClick={save}
                disabled={!selectedPath}
                className="flex items-center gap-1.5 bg-accent text-bg text-[12px] font-medium px-3 py-1.5 rounded-lg disabled:opacity-40"
              >
                <Save size={13} /> Save
              </button>
            </div>
          </div>
          <div className="flex-1 overflow-auto">
            {selectedPath ? (
              <CodeMirror
                value={content}
                height="100%"
                theme={oneDark}
                extensions={languageFor(selectedPath)}
                onChange={(value) => setContent(value)}
              />
            ) : (
              <div className="flex items-center justify-center h-full text-dim text-[13px]">
                Select a file to view or edit it
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
