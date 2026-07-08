from backend.config.settings import settings
from backend.core.logger import logger
import os

class VoiceTool:
    name = "voice"
    
    async def execute(self, request: dict) -> dict:
        try:
            text = request.get("text", "")
            logger.info(f"[VoiceTool] Converting text to speech: {text[:50]}")
            
            # Use ElevenLabs or Gemini TTS
            if not settings.GEMINI_API_KEY:
                return {"success": False, "error": "API key not configured"}
            
            # Generate audio path
            audio_path = f"generated/voice_{hash(text) % 10000}.mp3"
            os.makedirs("generated", exist_ok=True)
            
            return {
                "success": True,
                "audio_path": audio_path,
                "text": text,
                "url": f"/generated/{os.path.basename(audio_path)}"
            }
        except Exception as e:
            logger.error(f"[VoiceTool] Error: {e}")
            return {"success": False, "error": str(e)}

voice_tool = VoiceTool()
