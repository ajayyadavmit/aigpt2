from transformers import AutoModelForCausalLM, AutoTokenizer

local_model_path = "/Users/ajay/Desktop/Prod_Projects/models/aimodels"

try:
    tokenizer = AutoTokenizer.from_pretrained(local_model_path)
    model = AutoModelForCausalLM.from_pretrained(local_model_path)
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", str(e))
