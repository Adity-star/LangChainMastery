import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file (make sure to install python-dotenv)
load_dotenv()

# Try to retrieve the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    print("Error: API key is missing. Set the OPENAI_API_KEY environment variable.")
else:
    try:
        # Initialize the OpenAI model with configuration options
        llm = OpenAI(temperature=0.7, model_name="text-davinci-003", openai_api_key=openai_api_key)

        # Generate a response to a given prompt
        prompt = "Hello, LangChain! How are you today?"
        response = llm(prompt)

        # Print the response
        print(response)
    
    except Exception as e:
        print(f"Error: {str(e)}")
