from backend.master.planner import planner
from backend.master.dispatcher import dispatcher


class MasterAgent:

    async def process(
        self,
        message: str
    ):

        plan = planner.create_plan(message)

        return await dispatcher.dispatch(plan)


master_agent = MasterAgent()