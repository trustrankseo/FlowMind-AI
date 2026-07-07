from enum import Enum


class Intent(str, Enum):
    CHAT = "chat"
    CODE = "code"
    FILE = "file"
    BROWSER = "browser"
    SEARCH = "search"
    TEST = "test"
    IMAGE = "image"
    VIDEO = "video"
    VOICE = "voice"
    DEPLOY = "deploy"
    UNKNOWN = "unknown"


class IntentDetector:

    def detect(self, message: str) -> Intent:

        text = message.lower()

        if any(word in text for word in ["run test", "run the test", "pytest", "unit test", "run tests"]):
            return Intent.TEST

        if any(word in text for word in ["deploy", "release", "push to production", "go live"]):
            return Intent.DEPLOY

        if any(word in text for word in ["generate an image", "generate image", "draw", "picture of", "image of"]):
            return Intent.IMAGE

        if any(word in text for word in ["generate a video", "generate video", "make a video", "video of"]):
            return Intent.VIDEO

        if any(word in text for word in ["read this out loud", "text to speech", "say this", "speak this"]):
            return Intent.VOICE

        if any(word in text for word in ["code", "python", "javascript"]):
            return Intent.CODE

        if any(word in text for word in ["file", "read", "open"]):
            return Intent.FILE

        if any(word in text for word in ["browser", "website", "url"]):
            return Intent.BROWSER

        if any(word in text for word in ["search", "google"]):
            return Intent.SEARCH

        return Intent.CHAT


intent_detector = IntentDetector()