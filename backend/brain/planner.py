from backend.brain.intent import Intent


class TaskPlanner:

    def create_plan(self, intent: Intent):

        plans = {
            Intent.CHAT: ["provider"],

            Intent.CODE: [
                "coding_agent",
                "provider"
            ],

            Intent.FILE: [
                "file_tool",
                "provider"
            ],

            Intent.BROWSER: [
                "browser_tool",
                "provider"
            ],

            Intent.SEARCH: [
                "search_tool",
                "provider"
            ],

            Intent.TEST: [
                "testing_tool",
                "provider"
            ],

            Intent.IMAGE: [
                "image_tool"
            ],

            Intent.VIDEO: [
                "video_tool"
            ],

            Intent.VOICE: [
                "voice_tool"
            ],

            Intent.DEPLOY: [
                "deployment_tool"
            ]
        }

        return plans.get(intent, ["provider"])


planner = TaskPlanner()