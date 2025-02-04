# utils/document_loader.py

from langchain_community.document_loaders import PyPDFLoader

def load_and_split_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load_and_split()
