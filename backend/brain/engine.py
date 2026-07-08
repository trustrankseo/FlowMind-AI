from backend.interfaces.base_agent import BaseAgent
from backend.brain.intent import intent_detector
from backend.brain.planner import planner
from backend.brain.executor import executor
from backend.llm.orchestrator import orchestrator
from backend.core.logger import logger
import time

class BrainEngine(BaseAgent):
    name = "brain"

    async def process(self, message: str, context: str = ""):
        start_time = time.time()
        try:
            logger.info(f"[Brain] Processing: {message[:50]}")
            intent = intent_detector.detect(message)
            plan = planner.create_plan(intent)
            tool_results = await executor.execute(plan=plan, message=message)
            elapsed = time.time() - start_time
            return {
                "status": "success",
                "intent": intent.value,
                "plan": plan,
                "results": tool_results,
                "processing_time": elapsed
            }
        except Exception as error:
            logger.error(f"[Brain] Error: {error}")
            return {"status": "error", "error": str(error), "intent": "unknown", "results": []}

    async def handle(self, message: str):
        return await self.process(message)

brain = BrainEngine()
