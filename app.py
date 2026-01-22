import streamlit as st
import os
import shutil
from populate_database import load_documents, split_documents, add_to_chroma, clear_database
from query_data import query_rag

DATA_PATH = "data"

st.set_page_config(page_title="Lecture-Saver 3000", page_icon="🎓")

st.title("🎓 Lecture-Saver 3000")
st.markdown("### Your RAG-Based Academic Assistant")

# Sidebar for configuration and file upload
with st.sidebar:
    st.header("Configuration")
    if st.button("Reset Database"):
        clear_database()
        st.success("Database cleared!")
    
    st.header("Upload Lectures")
    uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
    
    if st.button("Process Documents"):
        if uploaded_files:
            if not os.path.exists(DATA_PATH):
                os.makedirs(DATA_PATH)
            
            for uploaded_file in uploaded_files:
                with open(os.path.join(DATA_PATH, uploaded_file.name), "wb") as f:
                    f.write(uploaded_file.getbuffer())
            
            with st.spinner("Processing..."):
                documents = load_documents()
                chunks = split_documents(documents)
                add_to_chroma(chunks)
            st.success("Documents processed and added to database!")
        else:
            st.warning("Please upload some PDF files first.")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about your lectures:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response, sources = query_rag(prompt)
                full_response = f"{response}\n\n**Sources:**\n" + "\n".join([f"- {s}" for s in sources])
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"An error occurred: {e}")
