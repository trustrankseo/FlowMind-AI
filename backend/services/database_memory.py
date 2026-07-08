from sqlalchemy.orm import Session
from backend.database.models.conversation import Conversation
from backend.database.models.message import Message
from backend.core.logger import logger

class DatabaseMemory:
    def create_conversation(self, db: Session, session_id: str) -> Conversation:
        try:
            conversation = db.query(Conversation).filter(
                Conversation.session_id == session_id
            ).first()
            
            if not conversation:
                conversation = Conversation(session_id=session_id)
                db.add(conversation)
                db.commit()
            
            return conversation
        except Exception as e:
            logger.error(f"[DatabaseMemory] Error creating conversation: {e}")
            db.rollback()
            return None
    
    def add_message(self, db: Session, conversation_id: int, role: str, content: str) -> Message:
        try:
            message = Message(
                conversation_id=conversation_id,
                role=role,
                content=content
            )
            db.add(message)
            db.commit()
            return message
        except Exception as e:
            logger.error(f"[DatabaseMemory] Error adding message: {e}")
            db.rollback()
            return None
    
    def get_conversation_messages(self, db: Session, conversation_id: int, limit: int = 50) -> list:
        try:
            messages = db.query(Message).filter(
                Message.conversation_id == conversation_id
            ).order_by(Message.created_at.desc()).limit(limit).all()
            return list(reversed(messages))
        except Exception as e:
            logger.error(f"[DatabaseMemory] Error retrieving messages: {e}")
            return []
    
    def get_conversation_history(self, db: Session, session_id: str, limit: int = 50) -> list:
        try:
            conversation = db.query(Conversation).filter(
                Conversation.session_id == session_id
            ).first()
            
            if not conversation:
                return []
            
            messages = self.get_conversation_messages(db, conversation.id, limit)
            return [
                {"role": msg.role, "content": msg.content, "timestamp": msg.created_at.isoformat()}
                for msg in messages
            ]
        except Exception as e:
            logger.error(f"[DatabaseMemory] Error getting history: {e}")
            return []

database_memory = DatabaseMemory()
