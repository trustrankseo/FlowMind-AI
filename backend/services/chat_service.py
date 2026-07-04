from sqlalchemy.orm import Session

from backend.models.chat import ChatResponse
from backend.providers.provider_manager import provider_manager
from backend.services.database_memory import database_memory


class ChatService:

    async def process(
        self,
        db: Session,
        session_id: str,
        message: str
    ):

        conversation = database_memory.create_conversation(
            db,
            session_id
        )

        database_memory.add_message(
            db,
            conversation.id,
            "user",
            message
        )

        provider = provider_manager.get_provider()

        reply = await provider.chat(message)

        database_memory.add_message(
            db,
            conversation.id,
            "assistant",
            reply
        )

        return ChatResponse(
            success=True,
            response=reply,
            session_id=session_id
        )


chat_service = ChatService()