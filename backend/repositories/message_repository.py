from backend.repositories.base import BaseRepository
from backend.database.models.message import Message


class MessageRepository(BaseRepository):

    def create(
        self,
        conversation_id: int,
        role: str,
        content: str
    ):

        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content
        )

        self.db.add(message)
        self.db.commit()

        return message

    def list(self, conversation_id: int):

        return (
            self.db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .all()
        )