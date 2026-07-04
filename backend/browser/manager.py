from backend.browser.actions import browser_actions


class BrowserManager:

    async def execute(
        self,
        request
    ):

        action = request.action.lower()

        if action == "open":

            return await browser_actions.open(
                request.url
            )

        if action == "click":

            return await browser_actions.click(
                request.selector
            )

        if action == "type":

            return await browser_actions.type(
                request.selector,
                request.text
            )

        if action == "screenshot":

            return await browser_actions.screenshot()

        return {
            "error": "Unknown Action"
        }


browser_manager = BrowserManager()