from backend.models.chat import ChatResponse
from backend.utils.memory import memory
from backend.providers.provider_manager import provider_manager


class ChatService:

    async def process(self, session_id: str, message: str):

        memory.add_message(session_id, "user", message)

        provider = provider_manager.get_provider()

        reply = await provider.chat(message)

        memory.add_message(session_id, "assistant", reply)

        return ChatResponse(
            success=True,
            response=reply
        )


chat_service = ChatService()