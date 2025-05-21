


"""_summary_
git clone https://github.com/Cornell-RelaxML/quip-sharp.git
pip install -r requirements.txt
cd quiptools && python setup.py install && cd ../
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from quantizer import QuipQuantizerc

model_name = "meta-llama/Llama-2-70b-hf"
quant_dir = "llama-70b_2bit_quip"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)

quant = QuipQuantizer(codebook="E8P12", dataset="redpajama")
quant.quantize_model(model, tokenizer, quant_dir)