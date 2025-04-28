from langchain_openai import OpenAI
from  dotenv import load_dotenv

load_dotenv()

# LLm Object for openai model
llm = OPenAI(model = 'gpt-3.5-turbo-instruct')

# Invoking the model with a query
result = llm.invoke('What is the capital of India?')

print(result)