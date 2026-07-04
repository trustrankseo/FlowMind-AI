from sqlalchemy.orm import Session

from backend.memory.repository import memory_repository


class SessionMemory:

    def history(
        self,
        db: Session,
        session_id: str
    ):

        conversation = memory_repository.get_conversation(
            db,
            session_id
        )

        if not conversation:
            return []

        return memory_repository.get_messages(
            db,
            conversation.id
        )


session_memory = SessionMemory()