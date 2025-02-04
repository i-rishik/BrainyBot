# utils/vector_store.py

from langchain_community.vectorstores import Chroma
from utils.embeddings import create_embeddings

def create_vector_store(texts):
    embeddings = create_embeddings()
    persist_directory = "vector_db"
    return Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)
