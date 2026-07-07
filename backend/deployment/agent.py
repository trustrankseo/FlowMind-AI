from backend.interfaces.base_agent import BaseAgent
from backend.deployment.tool import deployment_tool


class DeploymentAgent(BaseAgent):

    name = "deployment"

    async def handle(self, message):

        return await deployment_tool.execute({})


deployment_agent = DeploymentAgent()
