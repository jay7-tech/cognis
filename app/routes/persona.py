from fastapi import APIRouter, Request
from cognis.persona.graph_builder import build_persona_graph

router = APIRouter()

@router.get("/")
def get_persona_graph(request: Request):
    """
    Fetches the latest state of the Persona Knowledge Graph.
    Now uses a cached version for speed.
    """
    if hasattr(request.app.state, "persona_graph") and request.app.state.persona_graph:
        return request.app.state.persona_graph
        
    return {"nodes": [], "edges": []}
