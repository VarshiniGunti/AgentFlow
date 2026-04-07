from fastapi import APIRouter, HTTPException
from src.utils.schemas import QueryRequest, QueryResponse
from src.agents.orchestrator import OrchestratorAgent

router = APIRouter()
orchestrator = OrchestratorAgent()

@router.post("/query", response_model=QueryResponse)
async def process_user_query(request: QueryRequest):
    """
    Primary endpoint for processing user queries through the multi-agent system.
    """
    try:
        response = await orchestrator.process_query(request.prompt)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
