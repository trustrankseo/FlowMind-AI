from backend.models.chat import ChatResponse
from backend.utils.memory import memory
from backend.core.brain import brain


class ChatService:

    def process(self, session_id: str, message: str):

        memory.add_message(session_id, "user", message)

        result = brain.think(message)

        reply = result["reply"]

        memory.add_message(session_id, "assistant", reply)

        return ChatResponse(
            success=True,
            response=reply
        )


chat_service = ChatService()