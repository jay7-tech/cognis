# src/cognis/reasoning/temporal_patterns.py

from collections import defaultdict
from typing import List, Dict
from langchain_core.documents import Document


def track_pattern_over_time(
    documents: List[Document],
    window: str = "day"
) -> List[Dict]:
    """
    Tracks recurrence of semantic patterns over time.

    window: "day" | "week" | "month"
    """

    timeline = defaultdict(list)

    for doc in documents:
        timestamp = doc.metadata.get("timestamp")
        theme = doc.metadata.get("theme")

        if not timestamp or not theme:
            continue

        if window == "day":
            bucket = timestamp[:10]  # YYYY-MM-DD
        elif window == "month":
            bucket = timestamp[:7]   # YYYY-MM
        else:
            bucket = timestamp

        timeline[theme].append(bucket)

    trends = []
    for theme, buckets in timeline.items():
        trends.append({
            "theme": theme,
            "occurrences": len(buckets),
            "timeline": buckets
        })

    return sorted(trends, key=lambda x: x["occurrences"], reverse=True)
