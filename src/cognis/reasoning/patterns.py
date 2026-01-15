from collections import Counter

def detect_patterns(documents, min_occurrences=3):
    themes = []

    for doc in documents:
        theme = doc.metadata.get("theme")
        if theme:
            themes.append(theme)

    counts = Counter(themes)

    return {
        theme: count
        for theme, count in counts.items()
        if count >= min_occurrences
    }
