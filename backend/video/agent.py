from backend.interfaces.base_agent import BaseAgent
from backend.video.tool import video_tool


class VideoAgent(BaseAgent):

    name = "video"

    async def handle(self, message):

        request = message if isinstance(message, dict) else {"prompt": message}

        return await video_tool.execute(request)


video_agent = VideoAgent()
