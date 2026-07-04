from backend.tasks.models import TaskStatus


class TaskExecutor:

    async def execute(self, task):

        if task is None:
            return None

        task.status = TaskStatus.RUNNING

        # Future:
        # Coding Agent
        # Browser Agent
        # GitHub Agent

        task.status = TaskStatus.COMPLETED

        return task


task_executor = TaskExecutor()