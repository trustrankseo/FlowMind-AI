from backend.interfaces.base_tool import BaseTool
from backend.voice.speech import speech_generator


class VoiceTool(BaseTool):

    name = "voice"

    async def execute(self, request):

        text = ""

        if isinstance(request, dict):
            text = request.get("text", "")

        if not text:
            return {
                "success": False,
                "error": "No text provided for text-to-speech."
            }

        return await speech_generator.text_to_speech(text)


voice_tool = VoiceTool()
