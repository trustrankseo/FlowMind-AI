from backend.interfaces.base_agent import BaseAgent
from backend.testing.tool import testing_tool


class TestingAgent(BaseAgent):

    name = "testing"

    async def handle(self, message):

        request = message if isinstance(message, dict) else {}

        return await testing_tool.execute(request)


testing_agent = TestingAgent()
