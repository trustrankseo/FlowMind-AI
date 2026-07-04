class EnginePipeline:

    def steps(self):

        return [
            "memory",
            "planner",
            "workflow",
            "task_queue",
            "event_bus",
            "master_agent",
            "provider"
        ]


pipeline = EnginePipeline()