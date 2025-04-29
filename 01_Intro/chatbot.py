from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint   
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Create llm object for huggingface endpoint with repo_id and task(repo_id-model id in hugging face,task - what u want to do with model)
llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.2-1B",
    task = "text-generation"
)

# Create chat model object with llm object
model = ChatHuggingFace(llm = llm)

# Invoke the model with input - to store the chat history
chat_history = []

# Loop to chat with the model until user enters 'exit'
while True:
    user_input = input('Enter your query: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history)