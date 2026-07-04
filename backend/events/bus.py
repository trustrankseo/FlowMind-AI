class EventBus:

    def __init__(self):
        self._handlers = {}

    def subscribe(self, event_name: str, handler):

        self._handlers.setdefault(
            event_name,
            []
        ).append(handler)

    async def publish(
        self,
        event
    ):

        handlers = self._handlers.get(
            event.name,
            []
        )

        for handler in handlers:
            await handler(event)


event_bus = EventBus()