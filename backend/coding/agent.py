from backend.interfaces.base_agent import BaseAgent
from backend.coding.tool import coding_tool


class CodingAgent(BaseAgent):

    name = "coding"

    async def handle(self, message):

        return await coding_tool.execute(message)


coding_agent = CodingAgent()