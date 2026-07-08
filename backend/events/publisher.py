from backend.events.bus import event_bus
from backend.core.logger import logger
import time

class EventPublisher:
    async def publish(self, event_data: dict) -> None:
        try:
            if "type" not in event_data:
                raise ValueError("Event must have type")
            if "timestamp" not in event_data:
                event_data["timestamp"] = time.time()
            await event_bus.publish(event_data)
        except Exception as error:
            logger.error(f"[Publisher] Error: {error}")

    async def publish_error(self, error: Exception, context: str = "") -> None:
        await self.publish({"type": "error", "error": str(error), "context": context})

    async def publish_info(self, message: str, **kwargs) -> None:
        await self.publish({"type": "info", "message": message, **kwargs})

publisher = EventPublisher()
