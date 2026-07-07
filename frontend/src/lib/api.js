const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

async function request(path, options = {}) {

  const response = await fetch(`${BASE_URL}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });

  let data = null;

  try {
    data = await response.json();
  } catch {
    data = null;
  }

  if (!response.ok) {
    const message = data?.detail || data?.error || `Request failed (${response.status})`;
    throw new Error(message);
  }

  return data;
}

export const api = {
  baseUrl: BASE_URL,

  health: () => request("/health"),
  agents: () => request("/api/agents"),

  chat: (sessionId, message) =>
    request("/api/chat", {
      method: "POST",
      body: JSON.stringify({ session_id: sessionId, message }),
    }),

  history: (sessionId) => request(`/api/history/${sessionId}`),

  listFiles: (path = ".") =>
    request(`/api/files/list?path=${encodeURIComponent(path)}`),

  readFile: (path) =>
    request(`/api/files/read?path=${encodeURIComponent(path)}`),

  saveFile: (path, content) =>
    request("/api/files/save", {
      method: "POST",
      body: JSON.stringify({ path, content }),
    }),

  githubSummary: () => request("/api/github/summary"),

  runTests: (path = ".") =>
    request("/api/testing/run", {
      method: "POST",
      body: JSON.stringify({ path }),
    }),

  runDeployment: () =>
    request("/api/deployment/run", { method: "POST" }),

  generateImage: (prompt, numberOfImages = 1) =>
    request("/api/images/generate", {
      method: "POST",
      body: JSON.stringify({ prompt, number_of_images: numberOfImages }),
    }),

  generateVideo: (prompt) =>
    request("/api/video/generate", {
      method: "POST",
      body: JSON.stringify({ prompt }),
    }),

  textToSpeech: (text, voiceName = "Kore") =>
    request("/api/voice/speak", {
      method: "POST",
      body: JSON.stringify({ text, voice_name: voiceName }),
    }),

  recentLogs: (limit = 100) =>
    request(`/api/logs/recent?limit=${limit}`),
};
