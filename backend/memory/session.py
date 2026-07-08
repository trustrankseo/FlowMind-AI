from sqlalchemy.orm import Session as DBSession
from backend.database.models.message import Message
from backend.database.models.conversation import Conversation
from backend.core.logger import logger

class SessionMemory:
    def history(self, db: DBSession, session_id: str, limit: int = 20) -> list:
        try:
            conversation = db.query(Conversation).filter(Conversation.session_id == session_id).first()
            if not conversation:
                return []
            messages = db.query(Message).filter(Message.conversation_id == conversation.id).order_by(Message.created_at.desc()).limit(limit).all()
            return [{"role": msg.role, "content": msg.content} for msg in reversed(messages)]
        except Exception as error:
            logger.error(f"[SessionMemory] Error: {error}")
            return []

    def add(self, db: DBSession, session_id: str, role: str, content: str) -> None:
        try:
            conversation = db.query(Conversation).filter(Conversation.session_id == session_id).first()
            if not conversation:
                conversation = Conversation(session_id=session_id)
                db.add(conversation)
                db.commit()
            message = Message(conversation_id=conversation.id, role=role, content=content)
            db.add(message)
            db.commit()
        except Exception as error:
            logger.error(f"[SessionMemory] Error: {error}")
            db.rollback()

    def clear(self, db: DBSession, session_id: str) -> None:
        try:
            conversation = db.query(Conversation).filter(Conversation.session_id == session_id).first()
            if conversation:
                db.query(Message).filter(Message.conversation_id == conversation.id).delete()
                db.commit()
        except Exception as error:
            logger.error(f"[SessionMemory] Error: {error}")
            db.rollback()

session_memory = SessionMemory()
