from backend.engine.pipeline import pipeline
from backend.memory.session import session_memory
from backend.memory.summarizer import memory_summarizer
from backend.brain.engine import brain
from backend.providers.provider_manager import provider_manager
from backend.core.logger import logger
import time

class AIEngine:
    def __init__(self):
        self.name = "ai_engine"
        self.processing = False

    async def process(self, db, session_id: str, message: str):
        start_time = time.time()
        try:
            self.processing = True
            logger.info(f"[Engine] Processing for {session_id}")
            history = session_memory.history(db, session_id)
            memory = memory_summarizer.summarize(history)
            brain_result = await brain.process(message=message, context=memory)
            direct_result_intents = {"image", "video", "voice", "deploy"}
            if brain_result.get("intent") in direct_result_intents:
                results = brain_result.get("results") or []
                reply = str(results[0]) if results else "No result"
            else:
                reply = await self._build_reply(message, memory, brain_result)
            elapsed = time.time() - start_time
            return {
                "status": "success",
                "response": reply,
                "processing_time": elapsed,
                "session_id": session_id
            }
        except Exception as error:
            logger.error(f"[Engine] Error: {error}")
            return {"status": "error", "error": str(error)}
        finally:
            self.processing = False

    async def _build_reply(self, message: str, memory: str, brain_result: dict) -> str:
        try:
            results = brain_result.get("results") or []
            tool_context = ""
            if results:
                tool_context = f"\n\nResults: {results}"
            prompt = f"Memory: {memory}\nMessage: {message}{tool_context}\nReply:"
            provider = provider_manager.get_provider()
            return await provider.chat(prompt)
        except Exception as error:
            logger.error(f"[Engine] Reply error: {error}")
            return f"Error: {str(error)}"

engine = AIEngine()
