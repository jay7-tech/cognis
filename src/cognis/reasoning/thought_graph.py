# src/cognis/reasoning/thought_graph.py

import networkx as nx


def build_thought_graph(docs):
    """
    Builds a cognitive graph from memory.
    """

    G = nx.DiGraph()

    for d in docs:
        source = d.metadata.get("source", "unknown")
        content = d.page_content.strip()

        G.add_node(content, source=source)

        if source == "self_reflection":
            G.add_edge("reflection", content)
        elif source == "intervention":
            G.add_edge("intervention", content)

    return G
