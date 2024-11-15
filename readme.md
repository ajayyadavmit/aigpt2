# GPT 2 Model Files 

## ModelName : openai-community/gpt2


Certainly! If you've manually downloaded the GPT-2 model and want to use it in a Python script that you can run in Visual Studio Code (VSCode), here's how you can set everything up:

### Step-by-Step Guide for Using a Manually Downloaded GPT-2 Model in VSCode

1. **Assuming Your Folder Structure**:
   - You have downloaded the GPT-2 model files into a directory on your system, let's say `path/to/your/gpt2-model`.
   - The directory should contain files like:
     - `pytorch_model.bin`
     - `config.json`
     - `vocab.json`
     - `merges.txt`
     - `tokenizer.json`

### 2. Full Code for `app.py`

Here's the complete code to create a simple FastAPI server that uses the GPT-2 model:

4. **Run the FastAPI Server**:
   - In the VSCode terminal, start the server using `uvicorn`:
     ```bash
     uvicorn app:app --reload
     ```
   - This will start the FastAPI server, and you should see output indicating that the server is running at `http://127.0.0.1:8000`.

### 4. Testing the API
You can test the API using:
- **Browser**: Go to `http://127.0.0.1:8000/docs` to see the automatically generated API documentation and interact with the `/generate-text` endpoint.
- **Postman or Curl**: Send a `POST` request to `http://127.0.0.1:8000/generate-text` with a JSON body like:
  ```json
  {
    "prompt": "Once upon a time",
    "max_length": 100
  }
  ```

### Notes:
- **local_model_path**: Make sure to replace `"path/to/your/gpt2-model"` with the actual path where your GPT-2 model files are located on your system.
- **Customization**: You can customize `max_length` and other parameters as needed.

### Troubleshooting
- If you encounter any issues, double-check that all model files are in the correct directory and ensure you have the necessary permissions to access them.
- If you see errors related to missing dependencies, make sure all packages are installed correctly in your virtual environment.

This setup should work smoothly on your local system, and you can easily run and test it using VSCode!

