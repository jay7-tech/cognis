from fastapi import APIRouter, Request
from pydantic import BaseModel
from cognis.reasoning.self_reflection import reflect_and_store

router = APIRouter()

class ReflectionRequest(BaseModel):
    question: str

@router.post("/")
def reflect(request: Request, req: ReflectionRequest):
    response = reflect_and_store(
        question=req.question,
        retriever=request.app.state.retriever,
        vector_store=request.app.state.vector_store
    )
    return {"reflection": response}
