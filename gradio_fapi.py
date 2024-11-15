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


def generate_text(prompt, max_length=50):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"], max_length=max_length, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Create the Gradio interface
gradio_interface = gr.Interface(
    fn=generate_text,
    inputs=[gr.Textbox(lines=2, placeholder="Enter your prompt here..."), gr.Slider(
        10, 100, step=10, value=50, label="Max Length")],
    outputs="text",
    title="GPT-2 Text Generator"
)

# Set up the FastAPI app and mount the Gradio interface
app = FastAPI()
app = gr.mount_gradio_app(app, gradio_interface, path="/")

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
