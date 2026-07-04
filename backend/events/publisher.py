from backend.events.bus import event_bus
from backend.events.models import Event


class EventPublisher:

    async def emit(
        self,
        name: str,
        payload=None
    ):

        event = Event(
            name=name,
            payload=payload
        )

        await event_bus.publish(event)


publisher = EventPublisher()