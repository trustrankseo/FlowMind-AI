from backend.interfaces.base_agent import BaseAgent
from backend.images.tool import image_tool


class ImageAgent(BaseAgent):

    name = "image"

    async def handle(self, message):

        request = message if isinstance(message, dict) else {"prompt": message}

        return await image_tool.execute(request)


image_agent = ImageAgent()
