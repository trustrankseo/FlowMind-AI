from backend.interfaces.base_tool import BaseTool
from backend.coding.editor import editor


class CodingTool(BaseTool):

    name = "coding"

    async def execute(self, request):

        action = request.get("action")

        if action == "open":

            return editor.open(
                request["path"]
            )

        if action == "save":

            return editor.save(
                request["path"],
                request["content"]
            )

        return {
            "success": False,
            "error": "Unknown coding action."
        }


coding_tool = CodingTool()