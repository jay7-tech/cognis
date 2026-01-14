# src/memory/loader.py

from langchain.document_loaders import TextLoader
from typing import List

def load_text_documents(file_path: str) -> List:
    """
    Loads raw personal text data (notes, reflections, logs).
    """
    loader = TextLoader(file_path, encoding="utf-8")
    return loader.load()
