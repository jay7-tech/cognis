# src/cognis/memory/chunker.py

from langchain_text_splitters import RecursiveCharacterTextSplitter
from cognis.config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_documents(documents):
    """
    Splits documents into overlapping chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)
