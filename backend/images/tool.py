from backend.interfaces.base_tool import BaseTool
from backend.images.generator import image_generator


class ImageTool(BaseTool):

    name = "image"

    async def execute(self, request):

        prompt = ""

        if isinstance(request, dict):
            prompt = request.get("prompt", "")

        if not prompt:
            return {
                "success": False,
                "error": "No prompt provided for image generation."
            }

        return await image_generator.generate(prompt)


image_tool = ImageTool()
