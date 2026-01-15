from cognis.reasoning.reflection_chain import build_reflection_chain

def reflect_and_store(question, retriever, vector_store, embeddings):
    """
    Reflects on a question and stores the reflection back into memory.
    """

    reflection_chain = build_reflection_chain(retriever)

    reflection_message = reflection_chain.invoke(question)

    # ✅ FIX: extract text safely
    if hasattr(reflection_message, "content"):
        reflection_text = reflection_message.content
    else:
        reflection_text = str(reflection_message)

    vector_store.add_texts(
        [reflection_text],
        metadatas=[{"source": "self_reflection"}]
    )

    return reflection_text
