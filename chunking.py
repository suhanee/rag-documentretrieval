
import pickle
import faiss
import numpy as np
import requests
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT= "your_azure_openai_endpoint"
API_KEY= "your_api_key"

def get_embeddings(text_list):
    
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }
    payload = {"input": text_list}

    response = requests.post(AZURE_OPENAI_ENDPOINT, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Azure OpenAI API error: {response.json()}")

    return np.array([item["embedding"] for item in response.json()["data"]])

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def chunk_text(text, chunk_size=500, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap,
        separators=["\n\n", ".", "?", "!", "\n", " "], 
        length_function=len
    )
    return text_splitter.split_text(text)

if __name__ == "__main__":
    from extractor import extract_text_from_pdf

    # Path to the PDF file
    pdf_path = "uploaded_file.pdf"
    
    # Extract text
    document_text = extract_text_from_pdf(pdf_path)

    if not document_text.strip():
        print("Failed to extract any text from the document.")
    else:
        # Chunk text and get embeddings
        chunks = chunk_text(document_text)
        embeddings = get_embeddings(chunks)

        # Create FAISS index
        faiss_index = create_faiss_index(embeddings)

        # Save chunks to file
        with open("semantic_chunks.txt", "w") as f:
            for chunk in chunks:
                f.write(chunk + "\n")

        # Save FAISS index
        with open("faiss_index.pkl", "wb") as f:
            pickle.dump(faiss_index, f)

        print(f"Document text chunked into {len(chunks)} semantic parts.")
