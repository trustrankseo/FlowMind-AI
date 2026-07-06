from backend.tools.tool_manager import tool_manager


class TaskExecutor:

    async def execute(
        self,
        plan,
        message: str
    ):

        results = []

        for step in plan:

            if step == "provider":
                continue

            tool_name = (
                step
                .replace("_tool", "")
                .replace("_agent", "")
            )

            if tool_name not in tool_manager.available_tools():
                continue

            # NOTE (temporary fix): each tool currently expects a different
            # request shape (dict vs object-with-attributes), which isn't
            # standardized yet (see code review). Wrapping in try/except so
            # one tool's mismatched contract can't crash the whole request.
            try:
                result = await tool_manager.execute(
                    tool_name,
                    {
                        "action": "open",
                        "root": ".",
                        "path": message,
                        "url": message,
                        "content": message,
                    }
                )
            except Exception as error:
                result = {
                    "success": False,
                    "error": f"'{tool_name}' tool failed: {error}"
                }

            results.append(result)

        return results


executor = TaskExecutor()
