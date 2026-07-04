from backend.tasks.manager import task_manager
from backend.tasks.executor import task_executor
from backend.events.publisher import publisher


class WorkflowIntegration:

    async def execute_step(self, step):

        task = task_manager.create(
            name=step.name,
            data={
                "agent": step.agent
            }
        )

        await publisher.emit(
            "task.created",
            task.model_dump()
        )

        result = await task_executor.execute(task)

        await publisher.emit(
            "task.completed",
            result.model_dump()
        )

        return result


workflow_integration = WorkflowIntegration()