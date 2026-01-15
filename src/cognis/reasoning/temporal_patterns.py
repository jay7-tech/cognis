# src/cognis/reasoning/temporal_patterns.py

from datetime import datetime
from collections import defaultdict


def track_pattern_over_time(docs):
    """
    Tracks recurrence of patterns over time.
    """

    timeline = defaultdict(list)

    for d in docs:
        timestamp = d.metadata.get("timestamp", "unknown")
        content = d.page_content.lower()
        timeline[content].append(timestamp)

    trends = []
    for content, times in timeline.items():
        trends.append({
            "pattern": content,
            "occurrences": len(times),
            "timeline": times
        })

    return sorted(trends, key=lambda x: x["occurrences"], reverse=True)
