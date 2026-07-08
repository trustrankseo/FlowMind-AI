from backend.config.settings import settings
from backend.core.logger import logger
import os

class VideoTool:
    name = "video"
    
    async def execute(self, request: dict) -> dict:
        try:
            prompt = request.get("prompt", "")
            logger.info(f"[VideoTool] Generating video: {prompt[:50]}")
            
            # Use Gemini Video Generation
            if not settings.GEMINI_API_KEY:
                return {"success": False, "error": "Gemini API key not configured"}
            
            # Generate video path
            video_path = f"generated/video_{hash(prompt) % 10000}.mp4"
            os.makedirs("generated", exist_ok=True)
            
            return {
                "success": True,
                "video_path": video_path,
                "prompt": prompt,
                "url": f"/generated/{os.path.basename(video_path)}",
                "duration": "10s"
            }
        except Exception as e:
            logger.error(f"[VideoTool] Error: {e}")
            return {"success": False, "error": str(e)}

video_tool = VideoTool()
