from backend.tools.image_tool import image_tool
from backend.tools.video_tool import video_tool
from backend.tools.voice_tool import voice_tool
from backend.tools.testing_tool import testing_tool
from backend.tools.deployment_tool import deployment_tool
from backend.tools.file_tool import file_tool
from backend.core.logger import logger

class ToolManager:
    def __init__(self):
        self.tools = {
            "image": image_tool,
            "video": video_tool,
            "voice": voice_tool,
            "testing": testing_tool,
            "deployment": deployment_tool,
            "file": file_tool
        }
    
    async def execute(self, tool_name: str, request: dict) -> dict:
        tool = self.tools.get(tool_name)
        if not tool:
            logger.error(f"[ToolManager] Tool not found: {tool_name}")
            return {"success": False, "error": f"Tool not found: {tool_name}"}
        try:
            return await tool.execute(request)
        except Exception as e:
            logger.error(f"[ToolManager] Error executing {tool_name}: {e}")
            return {"success": False, "error": str(e)}
    
    def available_tools(self):
        return list(self.tools.keys())
    
    def get_tool(self, name: str):
        return self.tools.get(name)

tool_manager = ToolManager()
