# utils/qa_chain.py

from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

def create_qa_chain(vector_db):
    retriever = vector_db.as_retriever()
    llm = ChatGroq(model="llama-3.3-70b-Versatile", temperature=0.5)
    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
