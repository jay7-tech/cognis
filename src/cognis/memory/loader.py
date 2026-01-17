from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from typing import List
from cognis.utils.logging import trace_execution

PROJECT_ROOT = Path(__file__).resolve().parents[3]

@trace_execution
def load_text_documents(file_path: str, persona: str = "personal") -> List[Document]:
    # Resolve the path using the PROJECT_ROOT
    full_path = PROJECT_ROOT / file_path
    
    # Initialize the loader with the resolved path
    loader = TextLoader(str(full_path), encoding="utf-8")
    docs = loader.load()
    
    # Inject the persona into the metadata of each document
    for doc in docs:
        doc.metadata["persona"] = persona
        
    return docs