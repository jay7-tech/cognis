# src/cognis/reasoning/temporal_patterns.py

from collections import defaultdict
from typing import List, Dict
from langchain_core.documents import Document


from datetime import datetime

def track_pattern_over_time(
    documents: List[Document],
    window: str = "day"
) -> List[Dict]:
    """
    Tracks recurrence of semantic patterns over time.
    Improved for robustness: extracts theme from content if missing.
    """
    timeline = defaultdict(list)

    for doc in documents:
        # Fallback timestamp (now) if missing
        timestamp = doc.metadata.get("timestamp") or datetime.utcnow().isoformat()
        
        # Fallback theme: use first line or detect_patterns logic
        theme = doc.metadata.get("theme")
        if not theme:
            content = doc.page_content.strip()
            # Use a simple heuristic: first 30 chars of the first significant line
            lines = [l for l in content.splitlines() if len(l.strip()) > 5]
            theme = lines[0][:40] + "..." if lines else "General Thought"

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
