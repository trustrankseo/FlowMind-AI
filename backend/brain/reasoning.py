from backend.providers.provider_manager import provider_manager
from backend.core.logger import logger

class ReasoningEngine:
    async def analyze(self, message: str, context: str = "", intent = None) -> dict:
        try:
            prompt = f"Analyze: {message}\nIntent: {intent}\nContext: {context}"
            provider = provider_manager.get_provider()
            response = await provider.chat(prompt)
            return {
                "reasoning": response,
                "confidence": 0.8,
                "key_points": [],
                "next_steps": []
            }
        except Exception as error:
            logger.error(f"[Reasoning] Error: {error}")
            return {"reasoning": "", "confidence": 0.0, "key_points": [], "next_steps": []}

reasoning_engine = ReasoningEngine()
