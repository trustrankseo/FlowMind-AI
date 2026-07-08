from abc import ABC, abstractmethod
from backend.core.logger import logger

class BaseAgent(ABC):
    name: str = "agent"
    description: str = ""
    
    @abstractmethod
    async def execute(self, task: dict) -> dict:
        pass
    
    @abstractmethod
    async def handle(self, message: str) -> dict:
        pass
    
    def get_info(self) -> dict:
        return {"name": self.name, "description": self.description}
    
    def log(self, message: str):
        logger.info(f"[{self.name}] {message}")
