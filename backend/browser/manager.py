from backend.browser.actions import browser_actions


class BrowserManager:

    async def execute(
        self,
        request
    ):

        if request.action == "open":

            return await browser_actions.open(
                request.url
            )

        if request.action == "click":

            return await browser_actions.click(
                request.selector
            )

        if request.action == "type":

            return await browser_actions.type(
                request.selector,
                request.text
            )

        return "Unknown browser action."


browser_manager = BrowserManager()