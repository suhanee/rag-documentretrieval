from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

def extract_text_from_pdf(file):
    endpoint = "your_form_recognizer_endpoint"
    key = "your_api_key"
    
    client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    
    poller = client.begin_analyze_document("prebuilt-layout", file)
    result = poller.result()
    
    document_text = "\n".join([line.content for page in result.pages for line in page.lines])
    return document_text