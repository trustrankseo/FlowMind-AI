from backend.engine.pipeline import pipeline


class AIEngine:

    async def process(
        self,
        session_id: str,
        message: str
    ):

        return {
            "session_id": session_id,
            "message": message,
            "pipeline": pipeline.steps()
        }


engine = AIEngine()