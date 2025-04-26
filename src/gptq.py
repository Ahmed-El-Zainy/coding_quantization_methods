from transformers import AutoModelForCausalLM, AutoTokenizer, GPTQConfig


def init_gptq(model_id: str, quant_config: GPTQConfig):
    # Initialize the tokenizer using the specified model ID
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    # Initialize the model using the specified model ID and quantization configuration
    # The model is loaded with device mapping set to "auto"
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", quantization_config=quant_config)
    
    # Return the initialized model and tokenizer
    return model, tokenizer

if __name__=="__main__":
    