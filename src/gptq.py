from transformers import AutoModelForCausalLM, AutoTokenizer, GPTQConfig



def init_gptq(model_id: str):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    quant_config = GPTQConfig(bits=4, dataset = "c4", tokenizer=tokenizer)
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", quantization_config=quant_config)
    return model



if __name__ == "__main__":
     model_gptq = init_gptq()