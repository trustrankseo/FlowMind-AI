# backend/events/bus.py
from typing import Any, Callable, Dict, List
import asyncio
from pydantic import BaseModel

class Event(BaseModel):
    type: str
    data: Dict[str, Any]
    source: str
    timestamp: float

class EventBus:
    def __init__(self):
        self._listeners: Dict[str, List[Callable[[Event], None]]] = {}
        self._queue = asyncio.Queue()

    def subscribe(self, event_type: str, callback: Callable[[Event], None]):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    async def publish(self, event: Event):
        await self._queue.put(event)

    async def _process_event(self, event: Event):
        for callback in self._listeners.get(event.type, []):
            try:
                await callback(event)
            except Exception as e:
                # Production mein yahan logging aur metrics add karein
                print(f"EventBus callback error: {e}")

    async def run(self):
        while True:
            event = await self._queue.get()
            asyncio.create_task(self._process_event(event))

# Global instance
event_bus = EventBus()