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

# Tools
from backend.browser.tool import browser_tool
from backend.github.tool import github_tool
from backend.coding.tool import coding_tool
from backend.testing.tool import testing_tool
from backend.images.tool import image_tool
from backend.video.tool import video_tool
from backend.voice.tool import voice_tool
from backend.deployment.tool import deployment_tool

# Agents
from backend.browser.agent import browser_agent
from backend.github.agent import github_agent
from backend.coding.agent import coding_agent
from backend.testing.agent import testing_agent
from backend.images.agent import image_agent
from backend.video.agent import video_agent
from backend.voice.agent import voice_agent
from backend.deployment.agent import deployment_agent


def bootstrap():

    # ==========================
    # Register Core Services
    # ==========================

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

    # ==========================
    # Register Agents
    # ==========================

    agent_registry.register(
        brain.name,
        brain
    )

    agent_registry.register(
        browser_agent.name,
        browser_agent
    )

    agent_registry.register(
        github_agent.name,
        github_agent
    )

    agent_registry.register(
        coding_agent.name,
        coding_agent
    )

    agent_registry.register(
        testing_agent.name,
        testing_agent
    )

    agent_registry.register(
        image_agent.name,
        image_agent
    )

    agent_registry.register(
        video_agent.name,
        video_agent
    )

    agent_registry.register(
        voice_agent.name,
        voice_agent
    )

    agent_registry.register(
        deployment_agent.name,
        deployment_agent
    )

    # ==========================
    # Register Event Handlers
    # ==========================

    event_bus.subscribe(
        "task.created",
        log_event
    )

    event_bus.subscribe(
        "task.completed",
        task_completed
    )

    # ==========================
    # Register Tools
    # ==========================

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

    tool_manager.register(
        testing_tool.name,
        testing_tool
    )

    tool_manager.register(
        image_tool.name,
        image_tool
    )

    tool_manager.register(
        video_tool.name,
        video_tool
    )

    tool_manager.register(
        voice_tool.name,
        voice_tool
    )

    tool_manager.register(
        deployment_tool.name,
        deployment_tool
    )

    return container