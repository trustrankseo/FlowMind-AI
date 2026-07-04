from backend.planner.planner import planner
from backend.planner.executor import executor

from backend.providers.provider_manager import provider_manager

from backend.orchestrator.response import response_builder


class AIOrchestrator:

    async def run(
        self,
        memory,
        master_plan,
        message
    ):

        execution_plan = planner.create(
            goal=message,
            agents=[
                "brain",
                "coding",
                "browser",
                "github"
            ]
        )

        agent_results = await executor.execute(
            execution_plan
        )

        provider = provider_manager.get_provider()

        prompt = f"""
Memory:
{memory}

Master Plan:
{master_plan}

Execution Plan:
{execution_plan.model_dump()}

Agent Results:
{agent_results}

User:
{message}

Generate the best possible answer.
"""

        reply = await provider.chat(prompt)

        return response_builder.build(
            reply,
            {
                "execution_plan": execution_plan.model_dump(),
                "agent_results": agent_results
            }
        )


orchestrator = AIOrchestrator()