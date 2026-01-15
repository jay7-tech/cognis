# src/cognis/reasoning/reflection_chain.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from cognis.reasoning.llm import get_llm


def build_reflection_chain(retriever):
    """
    Builds a RAG + reflection chain using a local LLM.
    """

    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are Cognis, a personal reflective AI. "
                "You analyze the user's memories to help them understand patterns "
                "in their thoughts, struggles, and goals. Stay grounded in memory."
            ),
            (
                "human",
                """Relevant memory:
{context}

User question:
{question}

Give a thoughtful, reflective answer."""
            ),
        ]
    )

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
    )

    return chain
