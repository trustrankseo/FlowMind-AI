class AgentRegistry:

    def __init__(self):
        self._agents = {}

    def register(self, name: str, agent):
        self._agents[name] = agent

    def get(self, name: str):
        return self._agents.get(name)

    def all(self):
        return self._agents


agent_registry = AgentRegistry()