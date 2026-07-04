from backend.workflow.models import WorkflowStatus


class WorkflowExecutor:

    async def execute(
        self,
        workflow
    ):

        workflow.status = WorkflowStatus.RUNNING

        for step in workflow.steps:
            print(
                f"Executing {step.name} using {step.agent}"
            )

        workflow.status = WorkflowStatus.COMPLETED

        return workflow


executor = WorkflowExecutor()