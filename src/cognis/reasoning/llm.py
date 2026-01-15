# src/cognis/reasoning/llm.py

from langchain_community.llms import Ollama

def get_llm(model: str = "phi"):
    """
    Returns a local Ollama LLM.
    """
    return Ollama(
        model=model,
        temperature=0.3
    )
