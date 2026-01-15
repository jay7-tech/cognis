from datetime import datetime
from cognis.reasoning.reflection_chain import build_reflection_chain

def reflect_and_store(question, retriever, vector_store):
    """
    Reflects on a question and stores the reflection with timestamp metadata.
    """

    reflection_chain = build_reflection_chain(retriever)
    reflection = reflection_chain.invoke(question)

    vector_store.add_texts(
        [reflection.content],
        metadatas=[{
            "source": "self_reflection",
            "question": question,
            "timestamp": datetime.utcnow().isoformat()
        }]
    )

    return reflection.content
