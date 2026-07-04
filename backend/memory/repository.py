from sqlalchemy.orm import Session

from backend.database.models.conversation import Conversation
from backend.database.models.message import Message


class MemoryRepository:

    def get_conversation(
        self,
        db: Session,
        session_id: str
    ):

        return db.query(
            Conversation
        ).filter(
            Conversation.session_id == session_id
        ).first()

    def get_messages(
        self,
        db: Session,
        conversation_id: int
    ):

        return db.query(
            Message
        ).filter(
            Message.conversation_id == conversation_id
        ).all()


memory_repository = MemoryRepository()