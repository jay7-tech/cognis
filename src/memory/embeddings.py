# src/memory/embeddings.py

from langchain.embeddings import HuggingFaceEmbeddings
from src.config import EMBEDDING_MODEL_NAME

def get_embedding_model():
    """
    Returns embedding model used for semantic memory.
    """
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME
    )
