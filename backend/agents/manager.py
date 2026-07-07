from datetime import datetime


class AgentManager:

    def __init__(self):
        self.agents = {}

    def register(self, name, description):
        self.agents[name] = {
            "description": description,
            "status": "ready",
            "created_at": datetime.now().isoformat()
        }

    def get_agents(self):
        return self.agents

    def get_agent(self, name):
        return self.agents.get(name)


manager = AgentManager()

manager.register(
    "Brain",
    "Detects intent and routes messages to the right tool/agent."
)

manager.register(
    "Coding Agent",
    "Opens and saves project files."
)

manager.register(
    "Browser Agent",
    "Automates browser tasks."
)

manager.register(
    "GitHub Agent",
    "Summarizes and inspects the connected GitHub repository."
)

manager.register(
    "Testing Agent",
    "Runs pytest against the project and reports real results."
)

manager.register(
    "Image Agent",
    "Generates images from a text prompt (Gemini/Imagen)."
)

manager.register(
    "Video Agent",
    "Generates short videos from a text prompt (Gemini/Veo)."
)

manager.register(
    "Voice Agent",
    "Converts text to spoken audio (Gemini TTS)."
)

manager.register(
    "Deployment Agent",
    "Pulls latest code and installs dependencies on the server."
)