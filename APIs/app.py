from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from transformers import pipeline

# Load environment variables
load_dotenv()

# Load your OpenAI API key if you still want to use OpenAI models
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# If you still want to add OpenAI routes
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

# Load Hugging Face models using the transformers library

# Essay generation model using Hugging Face
essay_model = pipeline("text-generation", model="gpt2")  # You can change the model here to a suitable Hugging Face model

# Poem generation model using Hugging Face
poem_model = pipeline("text-generation", model="gpt2")  # You can change this to a model suited for poems, e.g., "distilgpt2"

# Define prompts using Langchain
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5-year-old child with 100 words")

# Adding Hugging Face routes with Langchain
def huggingface_essay_chain(prompt, model):
    def run(input_data):
        prompt_text = prompt.format(topic=input_data['topic'])
        generated_text = model(prompt_text, max_length=150, num_return_sequences=1)
        return {"generated_text": generated_text[0]['generated_text']}
    
    return run

def huggingface_poem_chain(prompt, model):
    def run(input_data):
        prompt_text = prompt.format(topic=input_data['topic'])
        generated_text = model(prompt_text, max_length=150, num_return_sequences=1)
        return {"generated_text": generated_text[0]['generated_text']}
    
    return run

# Add Hugging Face routes
add_routes(
    app,
    huggingface_essay_chain(prompt1, essay_model),
    path="/essay"
)

add_routes(
    app,
    huggingface_poem_chain(prompt2, poem_model),
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
