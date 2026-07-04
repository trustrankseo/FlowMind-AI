from backend.engine.pipeline import pipeline

from backend.memory.session import session_memory
from backend.memory.summarizer import memory_summarizer

from backend.master.manager import master_agent

from backend.providers.provider_manager import provider_manager


class AIEngine:

    async def process(
        self,
        db,
        session_id: str,
        message: str
    ):

        # Load Memory
        history = session_memory.history(
            db,
            session_id
        )

        memory = memory_summarizer.summarize(
            history
        )

        # Create Execution Plan
        plan = await master_agent.process(
            message
        )

        provider = provider_manager.get_provider()

        prompt = f"""
You are FlowMind AI Core.

Memory:

{memory}

Execution Plan:

{plan}

User:

{message}

Generate the best possible response.
"""

        response = await provider.chat(
            prompt
        )

        return {
            "memory": memory,
            "plan": plan,
            "response": response,
            "pipeline": pipeline.steps()
        }


engine = AIEngine()