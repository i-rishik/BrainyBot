import os
import streamlit as st
from utils.document_loader import load_and_split_pdf
from utils.text_splitter import split_text
from utils.embeddings import create_embeddings
from utils.vector_store import create_vector_store
from utils.qa_chain import create_qa_chain

# Have to Set up API key for ChatGroq
os.environ["GROQ_API_KEY"] = "Paste_Created_API_Key"

st.title("BrainyBot-Y: Your AI Sidekick 🧠🤖")
st.write("Ask questions based on the uploaded document!")


uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if uploaded_file:
    file_path = os.path.join("data", uploaded_file.name)
    os.makedirs("data", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    pages = load_and_split_pdf(file_path)

    texts = split_text(pages)

    vector_db = create_vector_store(texts)

    qa_chain = create_qa_chain(vector_db)

    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.write(chat["content"])

    if prompt := st.chat_input("Enter your question:"):

        with st.chat_message("user"):
            st.write(prompt)

        st.session_state.chat_history.append({"role": "user", "content": prompt})

        response = qa_chain({"query": prompt})
        answer = response["result"]

        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.chat_history.append({"role": "assistant", "content": answer})
