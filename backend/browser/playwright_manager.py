from playwright.async_api import async_playwright


class PlaywrightManager:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    async def start(self):

        if self.browser:
            return

        self.playwright = await async_playwright().start()

        self.browser = await self.playwright.chromium.launch(
            headless=False
        )

        self.page = await self.browser.new_page()

    async def stop(self):

        if self.browser:
            await self.browser.close()

        if self.playwright:
            await self.playwright.stop()


playwright_manager = PlaywrightManager()