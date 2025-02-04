# utils/text_splitter.py

from langchain.text_splitter import CharacterTextSplitter

def split_text(pages):
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    return text_splitter.split_documents(pages)
