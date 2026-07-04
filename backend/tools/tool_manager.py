from backend.tools.registry import tool_registry
from backend.tools.dispatcher import tool_dispatcher


class ToolManager:

    def register(
        self,
        name: str,
        tool
    ):

        tool_registry.register(
            name,
            tool
        )

    async def execute(
        self,
        tool_name: str,
        request
    ):

        return await tool_dispatcher.execute(
            tool_name,
            request
        )

    def available_tools(self):

        return tool_registry.all()


tool_manager = ToolManager()