# Importing libraries and modules
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Loading the environment variables use openai API
load_dotenv()

# Creating an instance of the ChatOpenAI class (temp = gives the randomness in the output)
model = ChatOpenAI(model = 'gpt-4',temperature = 0)

# Invoking the model with a query
result = model.invoke('what is capital of India?')

print(result)

