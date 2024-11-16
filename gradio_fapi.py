import torch
import gradio as gr
from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM
import uvicorn

# Load the tokenizer and GPT-2 model
tokenizer = AutoTokenizer.from_pretrained(
    "/Users/ajay/Desktop/Prod_Projects/models/aimodels")
model = AutoModelForCausalLM.from_pretrained(
    "/Users/ajay/Desktop/Prod_Projects/models/aimodels")

# Define the text generation function


def generate_text(prompt, max_length=13000):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        # Lower temperature increases randomness
        inputs["input_ids"], max_length=max_length,     temperature=0.7,
        top_k=50,repetition_penalty=1.2,
        top_p=0.9, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Create the Gradio interface
gradio_interface = gr.Interface(
    fn=generate_text,
    inputs=[gr.Textbox(lines=10, placeholder="Enter your prompt here..."), gr.Slider(
        10, 1000, step=50, value=50, label="Max Length")],
    outputs="text",
    title="GPT-2 Text Generator"
)

# Set up the FastAPI app and mount the Gradio interface
app = FastAPI()
app = gr.mount_gradio_app(app, gradio_interface, path="/")

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
