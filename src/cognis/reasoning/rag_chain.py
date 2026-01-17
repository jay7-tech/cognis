from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from cognis.reasoning.llm import get_llm

def format_docs(docs):
    """
    Quality Step: Ensuring sources are tracked.
    """
    formatted = []
    for i, doc in enumerate(docs):
        top_text = f"Source {i+1} (From {doc.metadata.get('timestamp', 'unknown')}):\n{doc.page_content}"
        formatted.append(top_text)
    return "\n\n".join(formatted)

def create_rag_chain(retriever):
    """
    FAANG Level: Constructing a 'Traceable' RAG Chain.
    This uses LangChain Expr Language (LCEL).
    """
    llm = get_llm()

    template = """
    You are Cognis, a personal intelligence assistant.
    You use the user's past memories to answer their questions about themselves.
    
    SYSTEM CONTEXT (USER MEMORIES):
    {context}
    
    QUESTION: {question}
    
    INSTRUCTIONS:
    1. Base your answer ONLY on the provided memories.
    2. If the memory doesn't contain the answer, say you don't know it yet.
    3. Be insightful, concise, and helpful.
    4. Reference the source (e.g., "In your notes from Jan 1st...") if possible.
    
    ANSWER:
    """
    
    prompt = ChatPromptTemplate.from_template(template)

    # The actual chain logic
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return chain