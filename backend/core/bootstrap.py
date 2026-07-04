from backend.core.container import container

from backend.providers.provider_manager import provider_manager
from backend.tools.tool_manager import tool_manager
from backend.brain.engine import brain
from backend.services.chat_service import chat_service
from backend.events.bus import event_bus
from backend.events.handlers import log_event
from backend.agents.registry import agent_registry
from backend.brain.engine import brain

from backend.events.handlers import (
    log_event,
    task_completed
)
def bootstrap():

    container.register(
        "provider_manager",
        provider_manager
    )

    container.register(
        "tool_manager",
        tool_manager
    )

    container.register(
        "brain",
        brain
    )

    container.register(
        "chat_service",
        chat_service
    )

    return container

event_bus.subscribe(
    "task.created",
    log_event
)
agent_registry.register(
    "brain",
    brain
)
event_bus.subscribe(
    "task.completed",
    task_completed
)