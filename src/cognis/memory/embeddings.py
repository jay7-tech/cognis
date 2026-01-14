# src/cognis/memory/embeddings.py

from langchain_community.embeddings import HuggingFaceEmbeddings
from cognis.config import EMBEDDING_MODEL_NAME


def get_embedding_model():
    """
    Returns a sentence-transformer embedding model.
    """
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME
    )
