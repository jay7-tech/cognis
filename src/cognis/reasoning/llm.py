# src/cognis/reasoning/llm.py

from langchain_community.chat_models import ChatOllama

def get_llm(model: str = "phi"):
    """
    Returns a local Ollama LLM.
    """
    return ChatOllama(
        model=model,
        temperature=0.3
    )
