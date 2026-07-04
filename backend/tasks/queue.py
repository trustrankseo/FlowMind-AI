from collections import deque


class TaskQueue:

    def __init__(self):
        self.queue = deque()

    def add(self, task):
        self.queue.append(task)

    def get(self):

        if self.queue:
            return self.queue.popleft()

        return None

    def size(self):
        return len(self.queue)


task_queue = TaskQueue()