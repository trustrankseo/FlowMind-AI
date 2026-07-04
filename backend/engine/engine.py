from backend.engine.pipeline import pipeline

from backend.memory.session import session_memory
from backend.memory.summarizer import memory_summarizer

from backend.master.manager import master_agent
from backend.orchestrator.orchestrator import orchestrator


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
        # Master Agent Decision
        # ----------------------------
        master_plan = await master_agent.process(
            message
        )

        # ----------------------------
        # AI Orchestrator
        # ----------------------------
        result = await orchestrator.run(
            memory=memory,
            master_plan=master_plan,
            message=message
        )

        # ----------------------------
        # Final Engine Response
        # ----------------------------
        return {
            "memory": memory,
            "master_plan": master_plan,
            "response": result["response"],
            "data": result["data"],
            "pipeline": pipeline.steps()
        }


engine = AIEngine()