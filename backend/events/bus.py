# backend/events/bus.py
from typing import Any, Callable, Dict, List, Optional
import asyncio
import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class Event(BaseModel):
    type: str
    data: Dict[str, Any]
    source: str
    timestamp: float

class EventBus:
    def __init__(self):
        self._listeners: Dict[str, List[Callable[[Event], Any]]] = {}
        self._queue = asyncio.Queue()
        self._running = False
        self._task: Optional[asyncio.Task] = None

    def subscribe(self, event_type: str, callback: Callable[[Event], Any]):
        """
        Subscribe a callback to an event type.
        Callback can be sync or async (coroutine).
        """
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    def unsubscribe(self, event_type: str, callback: Callable[[Event], Any]):
        """
        Remove a callback from an event type.
        """
        if event_type in self._listeners:
            try:
                self._listeners[event_type].remove(callback)
            except ValueError:
                pass

    async def publish(self, event: Event):
        """
        Publish an event to the bus.
        """
        await self._queue.put(event)

    async def _process_event(self, event: Event):
        """
        Process a single event by calling all subscribed callbacks.
        Handles both sync and async callbacks.
        """
        for callback in self._listeners.get(event.type, []):
            try:
                result = callback(event)
                if asyncio.iscoroutine(result):
                    await result
            except Exception as e:
                logger.error(
                    f"EventBus callback error for event {event.type} from {event.source}: {e}",
                    exc_info=True
                )

    async def run(self):
        """
        Main event loop. Runs until stop() is called.
        """
        self._running = True
        while self._running:
            try:
                event = await self._queue.get()
                await self._process_event(event)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"EventBus run loop error: {e}", exc_info=True)

    async def start(self):
        """
        Start the event bus in the background.
        """
        if self._task is None or self._task.done():
            self._task = asyncio.create_task(self.run())

    async def stop(self):
        """
        Stop the event bus gracefully.
        """
        self._running = False
        if self._task and not self._task.done():
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass

# Global instance
event_bus = EventBus()