from backend.browser.playwright_manager import playwright_manager


class BrowserActions:

    async def open(self, url: str):

        await playwright_manager.start()

        await playwright_manager.page.goto(url)

        return {
            "success": True,
            "url": url
        }

    async def click(
        self,
        selector: str
    ):

        await playwright_manager.page.click(
            selector
        )

        return {
            "success": True
        }

    async def type(
        self,
        selector: str,
        text: str
    ):

        await playwright_manager.page.fill(
            selector,
            text
        )

        return {
            "success": True
        }

    async def screenshot(
        self,
        path="screenshot.png"
    ):

        await playwright_manager.page.screenshot(
            path=path
        )

        return path


browser_actions = BrowserActions()