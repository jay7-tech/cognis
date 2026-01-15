# src/cognis/reasoning/reflection_chain.py

from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from cognis.reasoning.llm import get_llm
from cognis.reasoning.prompts import REFLECTION_PROMPT


def build_reflection_chain(retriever):
    """
    Builds a reflection reasoning chain using LCEL (LangChain Expression Language)
    """

    llm = get_llm()

    def retrieve_context(question: str) -> str:
        docs = retriever.invoke(question)
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {
            "context": RunnableLambda(retrieve_context),
            "question": RunnablePassthrough(),
        }
        | REFLECTION_PROMPT
        | llm
    )

    return chain
