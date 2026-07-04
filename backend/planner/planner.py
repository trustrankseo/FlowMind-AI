from backend.planner.models import (
    ExecutionPlan,
    PlanStep,
)


class AIPlanner:

    def create(
        self,
        goal: str,
        agents: list
    ):

        plan = ExecutionPlan(
            goal=goal
        )

        plan.steps = [
            PlanStep(
                id=index + 1,
                title=f"Run {agent}",
                agent=agent
            )
            for index, agent in enumerate(agents)
        ]

        return plan


planner = AIPlanner()