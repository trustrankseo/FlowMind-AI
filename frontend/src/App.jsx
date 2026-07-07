import { Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import ChatPage from "./pages/ChatPage";
import FilesPage from "./pages/FilesPage";
import BrowserPage from "./pages/BrowserPage";
import GitHubPage from "./pages/GitHubPage";
import ImagePage from "./pages/ImagePage";
import VideoPage from "./pages/VideoPage";
import VoicePage from "./pages/VoicePage";
import TestingPage from "./pages/TestingPage";
import DeploymentPage from "./pages/DeploymentPage";
import LogsPage from "./pages/LogsPage";

export default function App() {
  return (
    <div className="flex min-h-screen bg-bg text-white">
      <Sidebar />
      <main className="flex-1 p-6 h-screen overflow-y-auto">
        <Routes>
          <Route path="/" element={<ChatPage />} />
          <Route path="/files" element={<FilesPage />} />
          <Route path="/browser" element={<BrowserPage />} />
          <Route path="/github" element={<GitHubPage />} />
          <Route path="/image" element={<ImagePage />} />
          <Route path="/video" element={<VideoPage />} />
          <Route path="/voice" element={<VoicePage />} />
          <Route path="/testing" element={<TestingPage />} />
          <Route path="/deployment" element={<DeploymentPage />} />
          <Route path="/logs" element={<LogsPage />} />
        </Routes>
      </main>
    </div>
  );
}
