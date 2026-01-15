# src/cognis/reasoning/reflection_chain.py

from langchain_core.runnables import RunnablePassthrough
from cognis.reasoning.llm import get_llm
from cognis.reasoning.prompts import REFLECTION_PROMPT


def build_reflection_chain(retriever):
    """
    Builds a loop-aware reflection chain using memory + LLM reasoning.
    """

    llm = get_llm()

    def retrieve_context(question: str) -> str:
        docs = retriever.invoke(question)
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {
            "context": retrieve_context,
            "question": RunnablePassthrough()
        }
        | REFLECTION_PROMPT
        | llm
    )

    return chain
