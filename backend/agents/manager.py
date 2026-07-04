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
    "Master Agent",
    "Controls all FlowMind AI agents."
)

manager.register(
    "Coding Agent",
    "Writes and analyzes code."
)

manager.register(
    "Browser Agent",
    "Automates browser tasks."
)

manager.register(
    "Research Agent",
    "Searches and summarizes information."
)

manager.register(
    "File Agent",
    "Reads and manages project files."
)

manager.register(
    "Task Planner",
    "Creates execution plans and manages tasks."
)