import streamlit as st
from langchain_community.vectorstores import Chroma

def inspect_chroma_db(vector_store):
    st.sidebar.markdown("### Chroma DB Inspector")
    
    try:
        doc_count = vector_store._collection.count()
        st.sidebar.success(f"Document stored in the vector database.")
    except Exception as e:
        st.sidebar.error(f"Error accessing vector store: {e}")
    
    query = st.sidebar.text_input("Search Documents", "")
    if query:
        try:
            results = vector_store.similarity_search(query,k=3)
            st.sidebar.write(f"Found {len(results)} results:")
            for i, doc in enumerate(results):
                st.sidebar.write(f"**result {i + 1}. {doc.page_content[:200]}...")  # Display first 200 characters of each document
        except Exception as e:
            st.sidebar.error(f"Error during search: {e}")
    else:
        st.sidebar.write("Enter a query to search documents.")