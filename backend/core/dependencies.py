from backend.providers.provider_manager import provider_manager
from backend.tools.tool_manager import tool_manager
from backend.brain.engine import brain
from backend.services.chat_service import chat_service


def get_provider():
    return provider_manager


def get_tool_manager():
    return tool_manager


def get_brain():
    return brain


def get_chat_service():
    return chat_service