# my_text_generator.py

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Initialize the OpenAI model with desired parameters
llm = OpenAI(temperature=0.7, model_name="text-davinci-003")

# Create a prompt template
template = PromptTemplate(
    input_variables=["user_input"],
    template="You are a creative assistant. Answer the following:\n{user_input}"
)

# Take input from the user
user_input = input("Enter your question or prompt: ")

# Format the prompt
prompt = template.format(user_input=user_input)

# Get the response from the LLM
response = llm(prompt)

# Print the result
print("\nAI Response:\n", response)

