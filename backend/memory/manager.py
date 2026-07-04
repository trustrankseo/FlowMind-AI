from typing import Dict, List

from backend.memory.models import MemoryItem


class MemoryManager:

    def __init__(self):
        self.memory: Dict[str, List[MemoryItem]] = {}

    def save(self, item: MemoryItem):

        if item.session_id not in self.memory:
            self.memory[item.session_id] = []

        self.memory[item.session_id].append(item)

    def get(self, session_id: str):

        return self.memory.get(session_id, [])

    def clear(self, session_id: str):

        self.memory[session_id] = []


memory_manager = MemoryManager()