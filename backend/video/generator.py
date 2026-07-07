import os
import uuid
import asyncio

from google import genai

from backend.config.settings import settings
from backend.core.logger import logger


class VideoGenerator:

    def __init__(self, output_dir: str = "generated/videos"):

        self._client = None
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def _get_client(self):

        if self._client is None:

            if not settings.GEMINI_API_KEY:
                raise ValueError(
                    "GEMINI_API_KEY is not set. Add it to your .env file."
                )

            self._client = genai.Client(
                api_key=settings.GEMINI_API_KEY
            )

        return self._client

    async def generate(
        self,
        prompt: str,
        poll_seconds: int = 10,
        timeout_seconds: int = 300
    ):

        try:

            client = self._get_client()

            operation = await client.aio.models.generate_videos(
                model=settings.GEMINI_VIDEO_MODEL,
                prompt=prompt
            )

            elapsed = 0

            while not operation.done:

                if elapsed >= timeout_seconds:
                    return {
                        "success": False,
                        "error": f"Video generation timed out after {timeout_seconds}s."
                    }

                await asyncio.sleep(poll_seconds)
                elapsed += poll_seconds

                operation = await client.aio.operations.get(operation)

            saved_paths = []

            for generated_video in operation.response.generated_videos:

                filename = f"{uuid.uuid4().hex}.mp4"
                filepath = os.path.join(self.output_dir, filename)

                await client.aio.files.download(
                    file=generated_video.video
                )

                generated_video.video.save(filepath)

                saved_paths.append(filepath)

            return {
                "success": True,
                "prompt": prompt,
                "videos": saved_paths
            }

        except Exception as error:

            logger.error(f"[VideoGenerator] request failed: {error}")

            return {
                "success": False,
                "error": f"Video generation failed: {error}"
            }


video_generator = VideoGenerator()
