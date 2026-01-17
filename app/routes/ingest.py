from fastapi import APIRouter, Request
from pydantic import BaseModel
from cognis.memory.loader import load_text_documents
from cognis.memory.chunker import chunk_documents
from cognis.memory.vectorstore import build_vector_store
from cognis.memory.embeddings import get_embedding_model

router = APIRouter()

class IngestRequest(BaseModel):
    file_path: str

from cognis.persona.graph_builder import build_persona_graph

@router.post("/")
def ingest(request: Request, req: IngestRequest):
    docs = load_text_documents(req.file_path)
    chunks = chunk_documents(docs)

    embeddings = get_embedding_model()
    vector_store = build_vector_store(chunks, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    
    # ✅ CACHE GRAPH TO SPEED UP UI
    # We use a summarized view to build the graph
    base_docs = retriever.invoke("Extract core habits, goals, and emotional states.")
    request.app.state.persona_graph = build_persona_graph(base_docs)
    
    request.app.state.vector_store = vector_store
    request.app.state.retriever = retriever

    return {"status": "ingested", "chunks": len(chunks)}
