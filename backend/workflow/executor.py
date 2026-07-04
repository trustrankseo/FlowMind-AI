from backend.workflow.integration import workflow_integration
from backend.workflow.models import WorkflowStatus


class WorkflowExecutor:

    async def execute(self, workflow):

        workflow.status = WorkflowStatus.RUNNING

        for step in workflow.steps:

            await workflow_integration.execute_step(step)

        workflow.status = WorkflowStatus.COMPLETED

        return workflow


executor = WorkflowExecutor()