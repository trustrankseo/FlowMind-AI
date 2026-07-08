from backend.agents.github_agent import github_agent
from backend.agents.browser_agent import browser_agent
from backend.agents.coding_agent import coding_agent
from backend.core.logger import logger

class AgentManager:
    def __init__(self):
        self.agents = {
            "github": github_agent,
            "browser": browser_agent,
            "coding": coding_agent
        }
    
    def get_agent(self, name: str):
        agent = self.agents.get(name)
        if not agent:
            logger.warning(f"[AgentManager] Agent not found: {name}")
            return None
        return agent
    
    def get_agents(self):
        return list(self.agents.keys())
    
    async def execute_agent(self, agent_name: str, task: dict) -> dict:
        agent = self.get_agent(agent_name)
        if not agent:
            return {"success": False, "error": f"Agent not found: {agent_name}"}
        try:
            return await agent.execute(task)
        except Exception as e:
            logger.error(f"[AgentManager] Execution error: {e}")
            return {"success": False, "error": str(e)}
    
    def get_agent_info(self, name: str):
        agent = self.get_agent(name)
        if not agent:
            return None
        return agent.get_info()
    
    def get_all_agents_info(self):
        return [self.get_agent_info(name) for name in self.get_agents()]

manager = AgentManager()
