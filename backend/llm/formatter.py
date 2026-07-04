import json


class Formatter:

    def parse(self, response: str):

        try:

            return json.loads(response)

        except Exception:

            return {
                "tool": "chat",
                "action": "reply"
            }


formatter = Formatter()