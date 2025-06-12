import streamlit as st
import warnings
import logging
from module.pdf_handler import upload_pdf
from module.vectorstore import create_vector_store
from module.chroma_inspector import inspect_chroma_db
from module.chat import display_chat_history, handle_user_input, download_chat_history
from module.llm import get_llm_chain

warnings.filterwarnings("ignore")
logging.getLogger("tranformers").setLevel(logging.ERROR)

st.set_page_config(page_title="AskMyPDF - RAGBOT",
                   page_icon=":robot_face:", layout="wide")

# app title
st.title("AskMyPDF - RAGBOT 🤖")
st.subheader("AI Answers from Your PDFs in Seconds")

# upload pdf file and submit
uploaded_file,submit = upload_pdf()

# user submit to create vector store
if submit and uploaded_file:
    with st.spinner("Updating Vector Store.."): 
        vector_store = create_vector_store(uploaded_file)
        st.session_state.vector_store = vector_store
        
# display vector store inspector (chroma db)
if "vector_store" in st.session_state:
    vector_store = st.session_state.vector_store
    inspect_chroma_db(vector_store)
    
# display chat history
display_chat_history()

# handle user input and chat
if "vector_store" in st.session_state:
    handle_user_input(get_llm_chain(st.session_state.vector_store))

# download chat history
download_chat_history()
