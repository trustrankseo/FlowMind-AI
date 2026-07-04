from backend.interfaces.base_agent import BaseAgent
from backend.browser.manager import browser_manager


class BrowserAgent(BaseAgent):

    name = "browser"

    async def handle(self, message):

        return await browser_manager.execute(message)


browser_agent = BrowserAgent()