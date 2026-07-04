from sqlalchemy.orm import Session

from backend.models.chat import ChatResponse
from backend.providers.provider_manager import provider_manager
from backend.services.database_memory import database_memory
from backend.brain.engine import brain

from backend.memory.session import session_memory
from backend.memory.summarizer import memory_summarizer


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

        # Load Previous Memory
        history = session_memory.history(
            db,
            session_id
        )

        # Generate Memory Summary
        memory_summary = memory_summarizer.summarize(
            history
        )

        # Active AI Provider
        provider = provider_manager.get_provider()

        # Generate AI Response
        reply = await provider.chat(
            f"""
You are FlowMind AI.

Memory Summary:
{memory_summary}

Brain Analysis:
{brain_result}

User Message:
{message}

Generate the best possible response based on:
1. Memory Summary
2. Brain Analysis
3. User Message

If a tool is required, use the Brain Analysis.
Otherwise, reply naturally.
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