from fastapi import APIRouter
from cognis.reasoning.patterns import score_patterns
from cognis.memory.retriever import get_retriever

router = APIRouter()


@router.get("/")
def detect_patterns():
    retriever = get_retriever()
    docs = retriever.invoke("recurring thought patterns")
    return score_patterns(docs)
