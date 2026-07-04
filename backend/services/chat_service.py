from sqlalchemy.orm import Session

from backend.models.chat import ChatResponse
from backend.services.database_memory import database_memory
from backend.engine.engine import engine


class ChatService:

    async def process(
        self,
        db: Session,
        session_id: str,
        message: str
    ):

        # Create or Get Conversation
        conversation = database_memory.create_conversation(
            db,
            session_id
        )

        # Save User Message
        database_memory.add_message(
            db,
            conversation.id,
            "user",
            message
        )

        # Process Request Through AI Engine
        engine_result = await engine.process(
            db=db,
            session_id=session_id,
            message=message
        )

        # Final Response
        reply = engine_result["response"]

        # Save Assistant Response
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