from backend.memory.manager import memory_manager
from backend.memory.models import MemoryItem


class ProjectMemory:

    def save(
        self,
        session_id,
        project_name
    ):

        item = MemoryItem(
            session_id=session_id,
            category="project",
            key="name",
            value=project_name
        )

        memory_manager.save(item)


projects = ProjectMemory()