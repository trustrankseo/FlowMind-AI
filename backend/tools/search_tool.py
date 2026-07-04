from backend.tools.base import BaseTool


class SearchTool(BaseTool):

    name = "search"

    description = "Future internet search"

    async def execute(self, query=None):

        return f"Searching: {query}"