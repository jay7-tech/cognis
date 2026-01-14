# src/cognis/memory/retriever.py

from cognis.config import TOP_K


def get_retriever(vector_store, persona=None):
    if persona:
        return vector_store.as_retriever(
            search_kwargs={
                "k": TOP_K,
                "filter": {"persona": persona}
            }
        )
    return vector_store.as_retriever(search_kwargs={"k": TOP_K})

