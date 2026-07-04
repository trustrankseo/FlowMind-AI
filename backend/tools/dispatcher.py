from backend.tools.registry import tool_registry


class ToolDispatcher:

    async def execute(
        self,
        tool_name: str,
        request
    ):

        tool = tool_registry.get(tool_name)

        if tool is None:

            return {
                "success": False,
                "error": f"Tool '{tool_name}' not found."
            }

        return await tool.execute(request)


tool_dispatcher = ToolDispatcher()