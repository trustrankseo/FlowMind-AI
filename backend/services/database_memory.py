from sqlalchemy.orm import Session

from backend.database.models.conversation import Conversation
from backend.database.models.message import Message


class DatabaseMemory:

    def create_conversation(
        self,
        db: Session,
        session_id: str
    ):

        conversation = db.query(
            Conversation
        ).filter(
            Conversation.session_id == session_id
        ).first()

        if conversation:
            return conversation

        conversation = Conversation(
            session_id=session_id
        )

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    def add_message(
        self,
        db: Session,
        conversation_id: int,
        role: str,
        content: str
    ):

        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content
        )

        db.add(message)
        db.commit()

        return message


database_memory = DatabaseMemory()