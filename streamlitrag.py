import streamlit as st
import pickle
import numpy as np
import requests
from docx import Document
from chunking import chunk_text, get_embeddings, create_faiss_index  # Import from chunking.py
from extractor import extract_text_from_pdf  # Import from extractor.py
from search import search_query  # Import from search.py
from io import BytesIO
from format_doc import save_text_to_docx

# Azure OpenAI Configurations
endpoint = "<your_azure_openai_endpoint>"
api_key = " <your_api_key>"
gpt_deployment_id = "gpt-4o"
api_version = "2023-05-15"

def generate_response(context, format_type="text"):
    """Use GPT-4o to generate structured responses based on the specified format."""
    headers = {"Content-Type": "application/json", "api-key": api_key}
    prompt = f"Format and summarize this information as {format_type}:\n{context}"
    data = {"messages": [{"role": "system", "content": "You are a RAG-powered AI assistant."},
                          {"role": "user", "content": prompt}],
            "max_tokens": 700, "temperature": 0.7}
    response = requests.post(f"{endpoint}/openai/deployments/{gpt_deployment_id}/chat/completions?api-version={api_version}", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def save_to_word(content):
    """Save formatted content to an MS Word document and return it as a BytesIO buffer."""
    buffer = BytesIO()
    doc = Document()
    doc.add_paragraph(content)
    doc.save(buffer)
    buffer.seek(0)
    return buffer

# Streamlit App
st.title("RAG-powered Document Retrieval")
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    query = st.text_input("Enter your query:")
    format_option = st.selectbox("Choose output format:", ["Text", "Table", "Bulleted list", "Numbered list"])

    if st.button("Search"):
        extracted_text = extract_text_from_pdf(uploaded_file)
        chunks = chunk_text(extracted_text)  # Chunking extracted text
        embeddings = get_embeddings(chunks)  # Getting embeddings
        faiss_index = create_faiss_index(embeddings)  # Creating FAISS index
        results = search_query(query, faiss_index, chunks)
        formatted_output = generate_response("\n".join(results), format_option)
        st.write(formatted_output)
        docx_path = "output.docx"
        save_text_to_docx(formatted_output, query, docx_path)

        with open(docx_path, "rb") as f:
            docx_bytes = f.read()
        
        st.download_button(
            label="Download Response as Word",
            data=docx_bytes,
            file_name="formatted_response.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )