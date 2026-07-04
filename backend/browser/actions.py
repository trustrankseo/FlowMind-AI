class BrowserActions:

    async def open(self, url: str):

        return f"Opening {url}"

    async def click(self, selector: str):

        return f"Clicking {selector}"

    async def type(
        self,
        selector: str,
        text: str
    ):

        return f"Typing '{text}' into {selector}"


browser_actions = BrowserActions()