#this model will use anthrophic api key to get the response
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

# Creating an instance of the Chatanthropic class (temp = gives the randomness in the output)
model = ChatAnthropic(model = 'claude-3-5-sonet-20241022',temperature = 0)

# Invoking the model with a query
result = model.invoke('what is capital of India?')

print(result)