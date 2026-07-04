from backend.tools.base import BaseTool


class CodeTool(BaseTool):

    name = "code"

    description = "Code generator"

    async def execute(self, prompt=None):

        return f"Generate code for: {prompt}"