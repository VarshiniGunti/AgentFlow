from src.agents.base import BaseAgent
from src.agents.planner import PlannerAgent
from src.agents.task_agent import TaskAgent
from src.agents.calendar_agent import CalendarAgent
from src.agents.notes_agent import NotesAgent
from src.agents.research_agent import ResearchAgent
from src.utils.schemas import Action, QueryResponse
from typing import List, Any

class OrchestratorAgent(BaseAgent):
    """
    Coordinator Agent that manages the flow between the Planner and specialized Agents.
    """
    def __init__(self):
        super().__init__("OrchestratorAgent", "Coordinate multi-agent workflows")
        self.planner = PlannerAgent()
        self.agents = {
            "task": TaskAgent(),
            "calendar": CalendarAgent(),
            "notes": NotesAgent(),
            "research": ResearchAgent()
        }

    async def process_query(self, prompt: str) -> QueryResponse:
        """
        High-level entry point to process a user query.
        1. Consult Planner.
        2. Execute actions sequentially.
        3. Aggregate results and workflow trace.
        """
        self.logger.info("processing_query_start", prompt=prompt)
        
        workflow = ["planner.create_plan"]
        plan = await self.planner.create_plan(prompt)
        
        results = []
        
        for action in plan.actions:
            step_name = f"{action.agent}.{action.tool}"
            workflow.append(step_name)
            
            self.logger.info("executing_step", step=step_name, params=action.params)
            
            agent = self.agents.get(action.agent)
            if agent:
                try:
                    result = await agent.execute(action)
                    results.append({"step": step_name, "status": "success", "result": result})
                    self.logger.info("step_success", step=step_name)
                except Exception as e:
                    results.append({"step": step_name, "status": "error", "error": str(e)})
                    self.logger.error("step_failed", step=step_name, error=str(e))
            else:
                error_msg = f"Agent '{action.agent}' not found"
                results.append({"step": step_name, "status": "error", "error": error_msg})
                self.logger.error("agent_not_found", agent=action.agent)
                
        return QueryResponse(
            status="success",
            results=results,
            message="Multi-step workflow completed",
            plan_rationale=plan.rationale,
            workflow=workflow
        )

    async def execute(self, action: Action) -> Any:
        # Orchestrator's primary work is in process_query
        pass
