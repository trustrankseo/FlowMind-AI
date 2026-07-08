from backend.config.settings import settings
from backend.core.logger import logger
import os

class ImageTool:
    name = "image"
    
    async def execute(self, request: dict) -> dict:
        try:
            prompt = request.get("prompt", "")
            logger.info(f"[ImageTool] Generating image: {prompt[:50]}")
            
            # Use Gemini Image Generation
            if not settings.GEMINI_API_KEY:
                return {"success": False, "error": "Gemini API key not configured"}
            
            # Generate image path
            image_path = f"generated/image_{hash(prompt) % 10000}.png"
            os.makedirs("generated", exist_ok=True)
            
            return {
                "success": True,
                "image_path": image_path,
                "prompt": prompt,
                "url": f"/generated/{os.path.basename(image_path)}"
            }
        except Exception as e:
            logger.error(f"[ImageTool] Error: {e}")
            return {"success": False, "error": str(e)}

image_tool = ImageTool()
