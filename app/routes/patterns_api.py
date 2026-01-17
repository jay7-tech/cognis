from fastapi import APIRouter, Request
from cognis.reasoning.temporal_patterns import track_pattern_over_time

router = APIRouter()

@router.get("/temporal")
def temporal_patterns(request: Request):
    retriever = request.app.state.retriever
    if not retriever:
        return []

    docs = retriever.invoke(
        "What thoughts or themes keep repeating?"
    )

    return track_pattern_over_time(docs)
