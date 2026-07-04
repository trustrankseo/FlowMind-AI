from backend.workflow.planner import planner
from backend.workflow.executor import executor


class WorkflowEngine:

    async def run(
        self,
        name: str,
        tasks: list
    ):

        workflow = planner.create(
            name,
            tasks
        )

        return await executor.execute(
            workflow
        )


workflow_engine = WorkflowEngine()