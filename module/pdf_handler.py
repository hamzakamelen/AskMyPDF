import streamlit as st
import tempfile

def upload_pdf():
    with st.sidebar:
        st.header("Upload PDF")
        pdf_file = st.file_uploader("Upload PDF", type=["pdf"],accept_multiple_files=True)
        submit = st.button("Submit")
    return pdf_file,submit

def save_uploaded_file(uploaded_file):
    file_paths = []
    for file in uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file.read())
            file_paths.append(temp_file.name)
    return file_paths
    