class BrainResponse:

    def __init__(self, intent, tool=None):
        self.intent = intent
        self.tool = tool