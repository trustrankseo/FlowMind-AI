from backend.interfaces.base_agent import BaseAgent
from backend.voice.tool import voice_tool


class VoiceAgent(BaseAgent):

    name = "voice"

    async def handle(self, message):

        request = message if isinstance(message, dict) else {"text": message}

        return await voice_tool.execute(request)


voice_agent = VoiceAgent()
