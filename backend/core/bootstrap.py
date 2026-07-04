from backend.core.container import container

from backend.providers.provider_manager import provider_manager
from backend.tools.tool_manager import tool_manager
from backend.brain.engine import brain
from backend.services.chat_service import chat_service

from backend.events.bus import event_bus
from backend.events.handlers import (
    log_event,
    task_completed,
)

from backend.agents.registry import agent_registry

from backend.browser.tool import browser_tool
from backend.github.tool import github_tool
from backend.coding.tool import coding_tool


def bootstrap():

    # Register Core Services
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

    # Register Agents
    agent_registry.register(
        "brain",
        brain
    )

    # Register Event Handlers
    event_bus.subscribe(
        "task.created",
        log_event
    )

    event_bus.subscribe(
        "task.completed",
        task_completed
    )

    # Register Tools
    tool_manager.register(
        browser_tool.name,
        browser_tool
    )

    tool_manager.register(
        github_tool.name,
        github_tool
    )

    tool_manager.register(
        coding_tool.name,
        coding_tool
    )

    return container