from backend.repositories.base import BaseRepository
from backend.database.models.conversation import Conversation


class ConversationRepository(BaseRepository):

    def get_by_session(self, session_id: str):

        return (
            self.db.query(Conversation)
            .filter(Conversation.session_id == session_id)
            .first()
        )

    def create(self, session_id: str):

        conversation = Conversation(
            session_id=session_id
        )

        self.db.add(conversation)
        self.db.commit()
        self.db.refresh(conversation)

        return conversation