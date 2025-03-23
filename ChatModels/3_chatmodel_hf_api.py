# Using free huggingface api to generate text(open source model) simple chatbot
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Create llm object for huggingface endpoint with repo_id and task(repo_id-model id in hugging face,task - what u want to do with model)
llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)

# Create chat model object with llm object
model = ChatHuggingFace(llm = llm)

# Invoke the model with input
result = model.invoke(input('Enter your query: '))

print(result.content)
