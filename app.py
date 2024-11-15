from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

#AI App
# Initialize the FastAPI app
app = FastAPI()

# Specify the local path to your GPT-2 model
local_model_path = "/Users/ajay/Desktop/Prod_Projects/models/aimodels"

# Load the tokenizer and model from the local directory
tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model = AutoModelForCausalLM.from_pretrained(local_model_path)

# Initialize the text generation pipeline using the local model and tokenizer
text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Define a Pydantic model for the request body
class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 50

# Define an endpoint to generate text

@app.post("/generate-text")
async def generate_text(request: TextGenerationRequest):
    # Use the pipeline to generate text and explicitly set pad_token_id
    results = text_generator(
        request.prompt,
        max_length=request.max_length,
        pad_token_id=tokenizer.eos_token_id  # Explicitly setting pad_token_id
    )
    return {"generated_text": results[0]["generated_text"]}
