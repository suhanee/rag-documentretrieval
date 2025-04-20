
## Project Overview

This project is a Retrieval-Augmented Generation (RAG)-based framework designed to process and analyze documents. It is capable of performing various functionalities, including document extraction, chunking, search, and formatting content for use in Microsoft Word documents. The project also includes an optional Streamlit or Flask application for invoking the RAG framework.

## Key Functionalities

1. **Find Relevant PDF Files**:
   - Locate appropriate PDF files for the experiment from sources like Kaggle or GitHub.

2. **Document Extraction**:
   - Experiment with document extraction using Azure Document Intelligence or Python libraries.

3. **Chunking**:
   - Experiment with splitting large documents into smaller, manageable chunks for efficient processing.

4. **Search**:
   - Experiment with search functionality to retrieve relevant information from the processed data.

5. **Build RAG Framework**:
   - Develop a Retrieval-Augmented Generation framework for enhanced document processing and analysis.

6. **Content Formatting**:
   - Format the extracted and processed content for use in Microsoft Word documents (this functionality is implemented in a notebook).

7. **Optional Application**:
   - Build a Streamlit or Flask application to invoke the RAG framework for interactive use.


### Key Files and Directories

- **`.env`**: Contains environment variables for Azure OpenAI and Document Intelligence API configurations. After cloning please add your own .env file with the following essential keys.

# Azure Cognitive Search service endpoint
AZURE_SEARCH_SERVICE_ENDPOINT=

# Azure Cognitive Search admin key for authentication
AZURE_SEARCH_ADMIN_KEY=

# Name of the Azure Cognitive Search index
AZURE_SEARCH_INDEX=

# Azure OpenAI service endpoint for GPT-4o chat completions
AZURE_OPENAI_ENDPOINT=

# Azure OpenAI API key for authentication
AZURE_OPENAI_API_KEY=

# Deployment name and model details for embeddings in Azure OpenAI
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=
AZURE_OPENAI_EMBEDDING_MODEL_NAME=

# API version for Azure OpenAI service
AZURE_OPENAI_API_VERSION=

# Deployment name for the GPT-4o model
AZURE_OPENAI_DEPLOYMENT_NAME=

# Azure Document Intelligence API key for authentication
AZURE_DOCUMENT_INTELLIGENCE_KEY=

# Azure Document Intelligence service endpoint
AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT=

- **`chunking.py`**: Script for splitting large documents into smaller, manageable chunks for processing.
- **`extractor.py`**: Handles text extraction from PDF files.
- **`format_doc.py`**: Formats extracted data into structured documents.
- **`search.py`**: Implements search functionality over the processed data.
- **`streamlitrag.py`**: Streamlit-based application for interactive data exploration.
- **`requirements.txt`**: Lists Python dependencies required for the project.
- **`data/`**: Contains raw data files

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Set Up a Virtual Environment**
   python -m venv venv
   On Windows: venv\Scripts\activate

3. **Install Dependencies:**
   pip install -r requirements.txt

4. **Configure Environment Variables:**

    Update the .env file with your Azure OpenAI and Document Intelligence API keys and endpoints.

5. **Run the Application:**    
    For Streamlit-based exploration: streamlit run streamlitrag.py


## Key Features
Text Extraction: Extracts text from PDF files using Azure Document Intelligence.
Semantic Chunking: Splits large documents into smaller chunks for efficient processing.
Search Functionality: Enables querying over the processed data.
Data Visualization: Interactive exploration of geological and drilling data.


## Dependencies
Python 3.12 or higher
Azure AI Form Recognizer
FAISS for semantic search
Streamlit for interactive applications
