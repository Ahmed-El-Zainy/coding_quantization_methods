# Load model directly
from transformers import AutoModelForSequenceClassification

def llmInt8():
    model = AutoModelForSequenceClassification.from_pretrained("Alibaba-NLP/gte-multilingual-reranker-base",
                                                               device_map="auto", load_in_8bit=True,
                                                               trust_remote_code=True)
    
    return model