from fastapi import APIRouter
from pydantic import BaseModel
from cognis.memory.loader import load_text_documents
from cognis.memory.chunker import chunk_documents
from cognis.memory.vectorstore import build_vector_store
from cognis.memory.embeddings import get_embedding_model

router = APIRouter()

class IngestRequest(BaseModel):
    file_path: str

@router.post("/")
def ingest(req: IngestRequest):
    docs = load_text_documents(req.file_path)
    chunks = chunk_documents(docs)

    embeddings = get_embedding_model()
    vector_store = build_vector_store(chunks, embeddings)

    return {"status": "ingested", "chunks": len(chunks)}
