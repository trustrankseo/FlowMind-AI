from backend.engine.pipeline import pipeline

from backend.memory.session import session_memory
from backend.memory.summarizer import memory_summarizer

from backend.master.manager import master_agent
from backend.providers.provider_manager import provider_manager

from backend.planner.planner import planner
from backend.planner.executor import executor


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
        # Create Execution Plan
        # ----------------------------
        execution_plan = planner.create(
            goal=message,
            agents=[
                "brain",
                "coding",
                "browser",
                "github"
            ]
        )

        # ----------------------------
        # Execute Agents
        # ----------------------------
        agent_results = await executor.execute(
            execution_plan
        )

        # ----------------------------
        # AI Provider
        # ----------------------------
        provider = provider_manager.get_provider()

        prompt = f"""
You are FlowMind AI Core.

Conversation Memory:
{memory}

Master Decision:
{master_plan}

Execution Plan:
{execution_plan.model_dump()}

Agent Results:
{agent_results}

User Message:
{message}

Generate the best possible response.

Instructions:
- Use conversation memory if relevant.
- Consider the execution plan.
- Use agent results if available.
- Reply naturally and helpfully.
"""

        response = await provider.chat(
            prompt
        )

        return {
            "memory": memory,
            "master_plan": master_plan,
            "execution_plan": execution_plan.model_dump(),
            "agent_results": agent_results,
            "response": response,
            "pipeline": pipeline.steps()
        }


engine = AIEngine()