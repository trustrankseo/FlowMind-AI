from backend.workflow.models import (
    Workflow,
    WorkflowStep
)


class WorkflowPlanner:

    def create(
        self,
        name: str,
        tasks: list
    ):

        workflow = Workflow(name=name)

        workflow.steps = [
            WorkflowStep(
                name=task["name"],
                agent=task["agent"]
            )
            for task in tasks
        ]

        return workflow


planner = WorkflowPlanner()