from backend.interfaces.base_tool import BaseTool
from backend.testing.runner import test_runner


class TestingTool(BaseTool):

    name = "testing"

    async def execute(self, request):

        target = "."

        if isinstance(request, dict) and request.get("path"):
            target = request["path"]

        return await test_runner.run(target)


testing_tool = TestingTool()
