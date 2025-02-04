# utils/embeddings.py

from langchain_community.embeddings import HuggingFaceEmbeddings

def create_embeddings():
    return HuggingFaceEmbeddings()
