from backend.providers.base import BaseProvider


class OpenAIProvider(BaseProvider):

    async def chat(self, message: str):

        return f"[OpenAI] {message}"