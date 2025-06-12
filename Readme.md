# AskMyPDF - RAGBOT 🤖

This project implements a **Retrieval-Augmented Generation (RAG)**-based chatbot that enables you to **upload PDFs** and **interact with them conversationally** using the **GROQ LLM** and an **in-memory Chroma vector store**.

---

## 🔧 Setup Instructions

### 1. Create and Activate a Virtual Environment

```bash
python -m venv askmypdf_ragbot
```

Activate the environment:

* **Windows**:

  ```bash
  askmypdf_ragbot\Scripts\activate
  ```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
askmypdf_ragbot/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # List of required Python packages
│
├── module/                   # Modular codebase
│   ├── pdf_handler.py        # Handles PDF upload and text extraction
│   ├── vectorstore.py        # Manages Chroma in-memory vector store
│   ├── llm.py                # GROQ LLM setup and RetrievalQA pipeline
│   ├── chat.py               # Handles user input/output and query flow
│   ├── chroma_inspector.py   # Sidebar tool to inspect document chunks
```

---

## 🚀 Features

* Upload and chat with **multiple PDF documents**
* Generate and store **document embeddings** using **Chroma** (in-memory)
* Leverage **GROQ LLM** with **RAG pipeline** for smart document Q\&A
* Inspect vector store **chunks directly from the Streamlit sidebar**
* Clean, modular code for easy extension and maintenance
