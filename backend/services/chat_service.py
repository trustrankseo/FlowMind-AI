from sqlalchemy.orm import Session
from backend.services.database_memory import database_memory
from backend.models.chat import ChatResponse
from backend.engine.engine import engine
from backend.core.logger import logger

class ChatService:
    async def process(self, db: Session, session_id: str, message: str) -> ChatResponse:
        try:
            logger.info(f"[ChatService] Processing message for {session_id}")
            
            # Create or get conversation
            conversation = database_memory.create_conversation(db, session_id)
            if not conversation:
                return ChatResponse(
                    success=False,
                    response="Failed to create conversation",
                    session_id=session_id
                )
            
            # Add user message
            database_memory.add_message(db, conversation.id, "user", message)
            
            # Process through engine
            engine_result = await engine.process(db, session_id, message)
            
            if engine_result.get("status") != "success":
                return ChatResponse(
                    success=False,
                    response=engine_result.get("error", "Processing failed"),
                    session_id=session_id
                )
            
            reply = engine_result.get("response", "No response")
            
            # Add assistant message
            database_memory.add_message(db, conversation.id, "assistant", reply)
            
            return ChatResponse(
                success=True,
                response=reply,
                session_id=session_id
            )
        except Exception as e:
            logger.error(f"[ChatService] Error: {e}")
            return ChatResponse(
                success=False,
                response=f"Error: {str(e)}",
                session_id=session_id
            )

chat_service = ChatService()
