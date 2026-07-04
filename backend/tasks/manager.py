import uuid

from backend.tasks.models import Task
from backend.tasks.queue import task_queue


class TaskManager:

    def create(
        self,
        name: str,
        data=None
    ):

        task = Task(
            id=str(uuid.uuid4()),
            name=name,
            data=data or {}
        )

        task_queue.add(task)

        return task

    def next(self):

        return task_queue.get()


task_manager = TaskManager()