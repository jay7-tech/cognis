# src/cognis/reasoning/patterns.py

from collections import Counter
from typing import List, Dict, Any
from langchain_core.documents import Document


def detect_patterns(
    documents: List[Document],
    min_occurrences: int = 2
) -> Dict[str, Any]:
    """
    Detect repeating cognitive / semantic patterns from stored documents.

    Returns:
    - recurring themes
    - frequency
    - severity score
    - confidence score
    """

    extracted_units = []

    for doc in documents:
        # 1️⃣ Prefer explicit theme if available
        theme = doc.metadata.get("theme")
        if theme:
            extracted_units.append(theme.lower().strip())
            continue

        # 2️⃣ Fallback: extract meaningful sentences from content
        content = doc.page_content or ""
        for line in content.splitlines():
            line = line.strip().lower()
            if len(line) > 25:  # avoid noise
                extracted_units.append(line)

    if not extracted_units:
        return {
            "patterns": [],
            "summary": {
                "total_documents": len(documents),
                "patterns_detected": 0
            }
        }

    counts = Counter(extracted_units)
    total_items = sum(counts.values())

    patterns = []

    for text, freq in counts.items():
        if freq >= min_occurrences:
            severity = round(freq / total_items, 3)
            confidence = round(min(freq / max(len(documents), 1), 1.0), 3)

            patterns.append({
                "pattern": text,
                "frequency": freq,
                "severity": severity,
                "confidence": confidence
            })

    patterns.sort(key=lambda x: x["frequency"], reverse=True)



    return {
        "patterns": patterns,
        "summary": {
            "total_documents": len(documents),
            "patterns_detected": len(patterns),
            "most_frequent": patterns[0]["pattern"] if patterns else None
        }
    }

# Backward-compatible alias for API usage
score_patterns = detect_patterns
