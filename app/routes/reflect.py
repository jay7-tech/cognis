from fastapi import APIRouter
from pydantic import BaseModel
from cognis.reasoning.self_reflection import reflect_and_store

router = APIRouter()

class ReflectionRequest(BaseModel):
    question: str

@router.post("/")
def reflect(req: ReflectionRequest):
    response = reflect_and_store(
        question=req.question,
        retriever=router.state.retriever,
        vector_store=router.state.vector_store
    )
    return {"reflection": response}
