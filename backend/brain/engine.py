from backend.brain.intent import intent_detector

from backend.brain.planner import planner

from backend.brain.executor import executor


class BrainEngine:

    async def process(self, message: str):

        intent = intent_detector.detect(
            message
        )

        plan = planner.create_plan(
            intent
        )

        results = await executor.execute(
            plan,
            message
        )

        return {
            "intent": intent.value,
            "plan": plan,
            "tool_results": results
        }


brain = BrainEngine()