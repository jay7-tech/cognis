# src/memory/vectorstore.py

from langchain.vectorstores import FAISS

def build_vector_store(chunks, embeddings):
    """
    Builds an in-memory FAISS vector store.
    """
    return FAISS.from_documents(chunks, embeddings)
