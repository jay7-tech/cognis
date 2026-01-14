# src/cognis/memory/retriever.py

from cognis.config import TOP_K


def get_retriever(vector_store):
    """
    Returns a retriever interface over vector memory.
    """
    return vector_store.as_retriever(
        search_kwargs={"k": TOP_K}
    )
