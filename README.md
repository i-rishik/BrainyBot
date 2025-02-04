# RAG-based Conversational QnA System 🤖📄
An AI-powered chatbot that leverages Retrieval-Augmented Generation (RAG) to provide accurate and context-aware answers from uploaded PDFs. Built with Streamlit, LangChain, and ChromaDB, it allows users to interact with documents in a conversational manner.

# ✨ Features
- **📂 Upload PDFs** – Ask questions based on document content.
- **🔍 Retrieval-Augmented Generation (RAG)** – Uses vector search for context-aware responses.
- **⚡ LLM-Powered Responses** – Integrates Groq's LLaMA-3 for smart answers.
- **🎨 User-Friendly UI** – Clean and intuitive Streamlit interface.

# 🚀 How It Works
1. Upload a PDF document.
2. The system processes and splits text into chunks.
3. The chunks are embedded and stored in a vector database (ChromaDB).
4. When you ask a question, the system retrieves relevant chunks.
5. A LLM **(Groq’s LLaMA-3)** generates a contextual response.

# 🛠️ Tech Stack
- Python 🐍
- Streamlit 🎨 (Frontend)
- LangChain 🔗 (LLM & Retrieval)
- ChromaDB 📚 (Vector Database)
- HuggingFace Embeddings 🤗
- **Groq LLaMA-3** 🦙 (LLM for responses)

## 📌 Installation & Setup

To get started with BrainyBot, you'll need to follow these installation steps:

1. Create a virtual environment and activate on your local machine to isolate the project's dependencies.

```bash
  python -m venv brainybot-env
  source brainy-env/bin/activate
```

2. Clone the repository:

```bash
git clone https://github.com/kalyan4270/BrainyBot.git
cd BrainyBot
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
   
``` bash
streamlit run app.py
```

# 🎯 Use Cases
- **Research Assistance 📑**
- **Legal Document Analysis ⚖️**
- **Academic Paper Summarization 🎓**
- **Business Reports Q&A 📊**

🚀 Try it now and revolutionize the way you interact with documents!
