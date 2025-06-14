from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from module.pdf_handler import save_uploaded_file
import os

PERSIST_DIR = "./chroma_store"

# def create_vector_store(uploaded_files):
#     paths = save_uploaded_file(uploaded_files)
#     docs = []
#     for paths in paths:
#         loader = PyPDFLoader(paths)
#         docs.extend(loader.load())
    
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#     text = text_splitter.split_documents(docs)
    
#     embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")
#     # embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    
#     # if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
#     vector_store = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
#     vector_store.add_documents(text)
#     vector_store.persist()
#     # else:
#     #     pass
#         # vector_store = Chroma.from_documents(text, embeddings, persist_directory=PERSIST_DIR)
#         # vector_store.persist()
#     return vector_store 


def create_vector_store(uploaded_files):
    if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
        # Use prebuilt vector store
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")
        vector_store = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
        return vector_store

    # Else, build new vector store
    paths = save_uploaded_file(uploaded_files)
    docs = []
    for path in paths:
        loader = PyPDFLoader(path)
        docs.extend(loader.load())
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text = text_splitter.split_documents(docs)
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")
    vector_store = Chroma.from_documents(text, embeddings, persist_directory=PERSIST_DIR)
    vector_store.persist()
    
    return vector_store
