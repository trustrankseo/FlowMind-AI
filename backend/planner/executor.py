from backend.agents.coordinator import coordinator


class PlanExecutor:

    async def execute(self, plan):

        results = []

        for step in plan.steps:

            result = await coordinator.assign(
                sender="planner",
                receiver=step.agent,
                action="execute",
                payload={}
            )

            results.append(result)

        return results


executor = PlanExecutor()