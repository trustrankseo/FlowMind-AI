import { NavLink } from "react-router-dom";
import {
  MessageSquare,
  FolderTree,
  Globe,
  GitFork,
  Image as ImageIcon,
  Video,
  Mic,
  FlaskConical,
  Rocket,
  ScrollText,
} from "lucide-react";

const NAV_ITEMS = [
  { to: "/", label: "Chat", icon: MessageSquare, end: true },
  { to: "/files", label: "Files & Editor", icon: FolderTree },
  { to: "/browser", label: "Browser", icon: Globe },
  { to: "/github", label: "GitHub", icon: GitFork },
  { to: "/image", label: "Image", icon: ImageIcon },
  { to: "/video", label: "Video", icon: Video },
  { to: "/voice", label: "Voice", icon: Mic },
  { to: "/testing", label: "Testing", icon: FlaskConical },
  { to: "/deployment", label: "Deployment", icon: Rocket },
  { to: "/logs", label: "Logs", icon: ScrollText },
];

export default function Sidebar() {
  return (
    <aside className="w-56 shrink-0 h-screen sticky top-0 bg-panel border-r border-line flex flex-col">
      <div className="flex items-center gap-2 px-4 py-4 border-b border-line">
        <div className="w-2.5 h-2.5 rounded-full bg-accent shadow-[0_0_8px_#5eead4]" />
        <span className="font-display font-semibold tracking-tight text-[15px]">
          FlowMind AI
        </span>
      </div>

      <nav className="flex-1 py-3 px-2 space-y-0.5 overflow-y-auto">
        {NAV_ITEMS.map(({ to, label, icon: Icon, end }) => (
          <NavLink
            key={to}
            to={to}
            end={end}
            className={({ isActive }) =>
              `flex items-center gap-2.5 px-3 py-2 rounded-lg text-[13.5px] transition-colors ${
                isActive
                  ? "bg-accentDim text-accent border border-accent/30"
                  : "text-dim hover:text-white hover:bg-panel2 border border-transparent"
              }`
            }
          >
            <Icon size={16} strokeWidth={2} />
            {label}
          </NavLink>
        ))}
      </nav>

      <div className="px-4 py-3 border-t border-line font-mono text-[10px] text-dim">
        v0.8.0 · self-hosted
      </div>
    </aside>
  );
}
