# src/cognis/reasoning/pattern_scoring.py

from collections import Counter
from typing import List
from langchain_core.documents import Document


def extract_memory_texts(docs: List[Document]) -> List[str]:
    """
    Extracts clean text from retrieved documents.
    """
    texts = []
    for d in docs:
        if hasattr(d, "page_content") and d.page_content:
            texts.append(d.page_content.strip())
    return texts


def score_patterns(
    retriever,
    query: str,
    k: int = 10
):
    """
    Detects repeating cognitive patterns by semantic retrieval.
    Returns frequency-ranked patterns.
    """

    # Retrieve semantically related memories
    docs = retriever.invoke(query)

    texts = extract_memory_texts(docs)

    if not texts:
        return {
            "status": "no_patterns",
            "message": "No repeating thoughts detected yet."
        }

    # Normalize + count
    normalized = [t.lower() for t in texts]
    counts = Counter(normalized)

    # Rank by recurrence
    ranked = [
        {
            "pattern": text,
            "frequency": freq
        }
        for text, freq in counts.most_common()
    ]

    return {
        "status": "patterns_detected",
        "query": query,
        "total_related_memories": len(texts),
        "patterns": ranked
    }
