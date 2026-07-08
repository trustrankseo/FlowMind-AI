from typing import Callable, Dict, List
from backend.core.logger import logger
import asyncio

class EventBus:
    def __init__(self):
        self._handlers: Dict[str, List[Callable]] = {}
        self._history: List[dict] = []
        self._max_history = 1000

    def subscribe(self, event_name: str, handler: Callable) -> Callable:
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(handler)
        logger.debug(f"[EventBus] Subscribed to {event_name}")
        def unsubscribe():
            self._handlers[event_name].remove(handler)
        return unsubscribe

    async def publish(self, event: dict) -> None:
        event_type = event.get("type", "unknown")
        logger.debug(f"[EventBus] Publishing {event_type}")
        self._add_to_history(event)
        handlers = self._handlers.get(event_type, [])
        if handlers:
            tasks = [handler(event) for handler in handlers]
            try:
                await asyncio.gather(*tasks)
            except Exception as error:
                logger.error(f"[EventBus] Error: {error}")

    def _add_to_history(self, event: dict) -> None:
        self._history.append(event)
        if len(self._history) > self._max_history:
            self._history = self._history[-self._max_history:]

    def get_history(self, limit: int = 100) -> list:
        return self._history[-limit:]

    def clear_history(self) -> None:
        self._history = []

event_bus = EventBus()
