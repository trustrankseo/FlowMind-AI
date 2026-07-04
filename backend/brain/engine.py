from backend.brain.intent import intent_detector
from backend.brain.planner import planner
from backend.brain.executor import executor

from backend.llm.orchestrator import orchestrator


class BrainEngine:

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


brain = BrainEngine()