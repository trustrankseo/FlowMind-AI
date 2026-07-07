import os
import uuid

from google import genai

from backend.config.settings import settings
from backend.core.logger import logger


class ImageGenerator:

    def __init__(self, output_dir: str = "generated/images"):

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

    async def generate(self, prompt: str, number_of_images: int = 1):

        try:

            client = self._get_client()

            response = await client.aio.models.generate_images(
                model=settings.GEMINI_IMAGE_MODEL,
                prompt=prompt,
                config={
                    "number_of_images": number_of_images
                }
            )

            saved_paths = []

            for generated_image in response.generated_images:

                filename = f"{uuid.uuid4().hex}.png"
                filepath = os.path.join(self.output_dir, filename)

                with open(filepath, "wb") as f:
                    f.write(generated_image.image.image_bytes)

                saved_paths.append(filepath)

            return {
                "success": True,
                "prompt": prompt,
                "images": saved_paths
            }

        except Exception as error:

            logger.error(f"[ImageGenerator] request failed: {error}")

            return {
                "success": False,
                "error": f"Image generation failed: {error}"
            }


image_generator = ImageGenerator()
