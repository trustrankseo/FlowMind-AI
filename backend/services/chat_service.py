
from sqlalchemy.orm import Session

from backend.models.chat import ChatResponse
from backend.providers.provider_manager import provider_manager
from backend.services.database_memory import database_memory
from backend.brain.engine import brain


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

        # AI Brain Analysis
        brain_result = await brain.process(message)

        # Active AI Provider
        provider = provider_manager.get_provider()

        # Generate AI Response
        reply = await provider.chat(
            f"""
You are FlowMind AI.

Brain Analysis:
{brain_result}

User Message:
{message}

Generate a helpful response based on the brain analysis.
"""
        )

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