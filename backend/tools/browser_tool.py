from backend.tools.base import BaseTool


class BrowserTool(BaseTool):

    name = "browser"

    description = "Browser automation"

    async def execute(self, url=None):

        return f"Open Browser: {url}"