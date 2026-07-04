from sqlalchemy.orm import Session

from backend.models.chat import ChatResponse
from backend.providers.provider_manager import provider_manager
from backend.services.database_memory import database_memory

from backend.memory.session import session_memory
from backend.memory.summarizer import memory_summarizer

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

        # Load Previous Memory
        history = session_memory.history(
            db,
            session_id
        )

        # Memory Summary
        memory_summary = memory_summarizer.summarize(
            history
        )

        # Central AI Engine
        engine_result = await engine.process(
            session_id=session_id,
            message=message
        )

        # Active AI Provider
        provider = provider_manager.get_provider()

        # Final AI Response
        reply = await provider.chat(
            f"""
You are FlowMind AI.

Memory Summary:
{memory_summary}

Engine Result:
{engine_result}

User Message:
{message}

Generate the best possible response.

Rules:
- Use memory if relevant.
- Follow the engine pipeline.
- If tools are required, follow the engine decision.
- Otherwise reply naturally.
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