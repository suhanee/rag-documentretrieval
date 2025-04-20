import pickle
import faiss
import numpy as np
import requests

# Azure OpenAI Configuration
endpoint = "your_azure_openai_endpoint"
api_key = "your_api_key"
embedding_deployment_id = "text-embedding-ada-002"
gpt_deployment_id = "gpt-4o"
api_version = "2023-05-15"

def get_embeddings(query):
    headers = {"Content-Type": "application/json", "api-key": api_key}
    data = {"input": query}
    response = requests.post(f"your_azure_openai_embeddings_endpoint", headers=headers, json=data)
    response.raise_for_status()
    return np.array(response.json()["data"][0]["embedding"]).reshape(1, -1)

def search_query(query, faiss_index, chunks, top_k=5):
    query_embedding = get_embeddings(query)
    distances, indices = faiss_index.search(query_embedding, top_k)
    results = [chunks[i] for i in indices[0]]
    return results

def expand_query(query):
    """Generate alternative query phrasings for better retrieval."""
    headers = {"Content-Type": "application/json", "api-key": api_key}
    data = {"messages": [{"role": "user", "content": f"Generate variations of this search query: {query}"}], "max_tokens": 50}
    response = requests.post(f"{endpoint}/openai/deployments/{gpt_deployment_id}/chat/completions?api-version={api_version}", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].split("\n")

def generate_response(context):
    """Generate structured response using GPT-4o."""
    headers = {"Content-Type": "application/json", "api-key": api_key}
    data = {"messages": [{"role": "system", "content": "You are a helpful assistant providing structured responses."},
                          {"role": "user", "content": f"Summarize and structure this information:\n{context}"}],
            "max_tokens": 200, "temperature": 0.7}
    response = requests.post(f"your_azure_openai_embeddings_endpoint", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def format_answer(results):
    context = "\n".join(results)
    response = generate_response(context)
    return response

if __name__ == "__main__":
    query = input("Enter your query: ")
    expanded_queries = expand_query(query)
    print("Expanded Queries:", expanded_queries)
    results = search_query(query)
    answer = format_answer(results)
    print("Answer:\n", answer)