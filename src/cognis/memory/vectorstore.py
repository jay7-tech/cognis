from cognis.utils.logging import trace_execution
from langchain_community.vectorstores import FAISS
import os

@trace_execution
def build_vector_store(chunks, embeddings, save_path: str = "data/processed/faiss_index"):
    """
    Builds and persists a FAISS vector store.
    """
    vector_store = FAISS.from_documents(chunks, embeddings)
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
    vector_store.save_local(save_path)
    return vector_store

@trace_execution
def load_vector_store(embeddings, load_path: str = "data/processed/faiss_index"):
    """
    Loads a persisted FAISS vector store.
    """
    if os.path.exists(load_path):
        return FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)
    return None
