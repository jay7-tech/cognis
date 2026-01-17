from fastapi import APIRouter, Request
from cognis.reasoning.intervention import generate_intervention

router = APIRouter()

from cognis.reasoning.planner import generate_behavioral_plan
from cognis.reasoning.temporal_patterns import track_pattern_over_time

@router.post("/")
def intervene(request: Request):
    retriever = request.app.state.retriever
    if not retriever:
        return {"status": "error", "message": "Retriever not initialized"}
        
    docs = retriever.invoke("What are the most urgent cognitive patterns to address?")
    if not docs:
        return {"status": "no_data", "intervention": "No patterns found to intervene on."}
        
    top = docs[0].page_content

    intervention = generate_intervention(
        pattern=top,
        frequency=3
    )

    return {"intervention": intervention}

@router.post("/plan")
def get_pro_plan(request: Request):
    retriever = request.app.state.retriever
    if not retriever:
        return {"status": "error", "message": "No active brain session"}
        
    docs = retriever.invoke("List every recurring habit and goal mentioned.")
    patterns = track_pattern_over_time(docs)
    
    plan = generate_behavioral_plan(patterns)
    return plan
