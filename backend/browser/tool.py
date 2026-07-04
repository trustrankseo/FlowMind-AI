from backend.interfaces.base_tool import BaseTool
from backend.browser.manager import browser_manager


class BrowserTool(BaseTool):

    name = "browser"

    async def execute(self, request):

        return await browser_manager.execute(
            request
        )


browser_tool = BrowserTool()