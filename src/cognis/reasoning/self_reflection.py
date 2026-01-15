# src/cognis/reasoning/self_reflection.py

from cognis.reasoning.reflection_chain import build_reflection_chain


def reflect_and_store(question, retriever, vector_store):
    """
    Reflects on a question and stores the reflection as long-term memory.
    """

    reflection_chain = build_reflection_chain(retriever)

    reflection = reflection_chain.invoke(question)

    # ✅ Convert to string explicitly
    reflection_text = str(reflection)

    vector_store.add_texts(
        texts=[reflection_text],
        metadatas=[{"source": "self_reflection"}]
    )

    return reflection_text
