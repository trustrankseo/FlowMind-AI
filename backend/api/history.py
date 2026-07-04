from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.database.models.conversation import Conversation
from backend.database.models.message import Message

router = APIRouter()


@router.get("/history/{session_id}")
async def history(
    session_id: str,
    db: Session = Depends(get_db)
):

    conversation = db.query(
        Conversation
    ).filter(
        Conversation.session_id == session_id
    ).first()

    if not conversation:
        return []

    messages = db.query(
        Message
    ).filter(
        Message.conversation_id == conversation.id
    ).all()

    return messages