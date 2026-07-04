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

            tool = tool_manager.get(
                step.replace("_tool", "")
            )

            if tool:

                result = await tool.execute(
                    prompt=message,
                    query=message,
                    path=message,
                    url=message
                )

                results.append(result)

        return results


executor = TaskExecutor()