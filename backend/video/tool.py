from backend.interfaces.base_tool import BaseTool
from backend.video.generator import video_generator


class VideoTool(BaseTool):

    name = "video"

    async def execute(self, request):

        prompt = ""

        if isinstance(request, dict):
            prompt = request.get("prompt", "")

        if not prompt:
            return {
                "success": False,
                "error": "No prompt provided for video generation."
            }

        return await video_generator.generate(prompt)


video_tool = VideoTool()
