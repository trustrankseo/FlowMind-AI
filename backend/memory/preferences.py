from backend.memory.manager import memory_manager
from backend.memory.models import MemoryItem


class PreferenceMemory:

    def save(
        self,
        session_id,
        key,
        value
    ):

        item = MemoryItem(
            session_id=session_id,
            category="preferences",
            key=key,
            value=value
        )

        memory_manager.save(item)


preferences = PreferenceMemory()