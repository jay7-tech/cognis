# src/cognis/reasoning/intervention.py

from cognis.reasoning.llm import get_llm


def generate_intervention(pattern, frequency):
    """
    Generates an actionable intervention for a repeated cognitive pattern.
    """

    llm = get_llm()

    prompt = f"""
You are a cognitive coach AI.

A user has repeated the following thought {frequency} times:

"{pattern}"

Your task:
1. Identify why this pattern may be repeating
2. Suggest ONE small, concrete intervention
3. Keep it practical, short, and non-judgmental

Respond clearly.
"""

    response = llm.invoke(prompt)
    return response
