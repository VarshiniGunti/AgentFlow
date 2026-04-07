from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class Action(BaseModel):
    """Represents a single structured action to be executed by an agent."""
    agent: str = Field(..., description="The type of agent: 'task', 'calendar', or 'notes'")
    tool: str = Field(..., description="The name of the tool/method to call (e.g. 'create_task', 'create_event')")
    params: Dict[str, Any] = Field(default_factory=dict, description="Parameters for the tool method")

class Plan(BaseModel):
    """A collection of actions to fulfill a user request."""
    actions: List[Action]
    rationale: str = Field(..., description="Explanation of why this plan was chosen")

class QueryRequest(BaseModel):
    """The incoming request schema for the /query endpoint."""
    prompt: str

class QueryResponse(BaseModel):
    """The outgoing response schema for the /query endpoint."""
    status: str
    results: List[Any]
    message: str
    plan_rationale: Optional[str] = Field(None, description="The rationale provided by the planner")
    workflow: Optional[List[str]] = Field(None, description="List of agent.tool steps executed")
