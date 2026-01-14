from pathlib import Path
from langchain_community.document_loaders import TextLoader
from typing import List

PROJECT_ROOT = Path(__file__).resolve().parents[3]

def load_text_documents(file_path: str) -> List:
    full_path = PROJECT_ROOT / file_path
    loader = TextLoader(str(full_path), encoding="utf-8")
    return loader.load()
