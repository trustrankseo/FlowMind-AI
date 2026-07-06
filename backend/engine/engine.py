from backend.engine.pipeline import pipeline

from backend.memory.session import session_memory
from backend.memory.summarizer import memory_summarizer

from backend.brain.engine import brain
from backend.providers.provider_manager import provider_manager


class AIEngine:

    async def process(
        self,
        db,
        session_id: str,
        message: str
    ):

        # ----------------------------
        # Load Conversation Memory
        # ----------------------------
        history = session_memory.history(
            db,
            session_id
        )

        memory = memory_summarizer.summarize(
            history
        )

        # ----------------------------
        # Brain: Intent Detection + Tool Execution
        #
        # NOTE (temporary fix): the previous flow routed through
        # master_agent -> orchestrator -> planner/executor -> coordinator,
        # which passed an AgentMessage object into brain.process() where a
        # plain string was expected, crashing every /api/chat call.
        # Calling brain directly here restores a working end-to-end path.
        # The multi-agent routing layer still needs a proper merge (see
        # code review) before it's reintroduced.
        # ----------------------------
        brain_result = await brain.process(message)

        reply = await self._build_reply(
            message,
            memory,
            brain_result
        )

        # ----------------------------
        # Final Engine Response
        # ----------------------------
        return {
            "memory": memory,
            "brain_result": brain_result,
            "response": reply,
            "data": brain_result,
            "pipeline": pipeline.steps()
        }

    async def _build_reply(
        self,
        message: str,
        memory: str,
        brain_result: dict
    ) -> str:

        results = brain_result.get("results") or []

        tool_context = ""

        if results:
            tool_context = f"\n\nTool results:\n{results}"

        prompt = (
            f"Conversation memory: {memory}\n\n"
            f"User message: {message}"
            f"{tool_context}\n\n"
            "Reply to the user's message directly and helpfully."
        )

        provider = provider_manager.get_provider()

        return await provider.chat(prompt)


engine = AIEngine()
