from backend.interfaces.base_agent import BaseAgent

from backend.brain.intent import intent_detector
from backend.brain.planner import planner
from backend.brain.executor import executor

from backend.llm.orchestrator import orchestrator


class BrainEngine(BaseAgent):

    name = "brain"

    async def process(
        self,
        message: str
    ):

        intent = intent_detector.detect(
            message
        )

        plan = planner.create_plan(
            intent
        )

        llm_decision = await orchestrator.select_tool(
            message
        )

        tool_results = await executor.execute(
            plan,
            message
        )

        return {
            "intent": intent.value,
            "plan": plan,
            "tool": llm_decision,
            "results": tool_results
        }

    async def handle(self, message):

        return await self.process(message)


brain = BrainEngine()