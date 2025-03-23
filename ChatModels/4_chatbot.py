from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser  # Output parser to parse the output(parse - convert the output to human readable format)

import streamlit as st  # for creating framework for web app
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

# This will enable tracing for your model and will help you to debug the model(langchain tracing)
os.environ["LANGCHAIN_TRACING_V2"]="true"

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Create a prompt for chatbot(what chatbot should say when it starts and what user should say)
prompt = ChatPromptTemplate.from_messages(
    [
        ('system','you are a chatbot.Please chat with me.'),
        ('user','Question:{question}')
    ]
)

# streamlit app framework
st.title('Chatbot')
input_text = st.text_input('Enter your question here:')

# Create llm object for openai model    
llm = ChatOpenAI(model='gpt-3.5-turbo')
output_parser = llm(prompt, input_text)

# chain of prompt, llm and output_parser to invoke the model in specific order
chain = prompt|llm|outpu_parser


# If input_text is not empty, invoke the model with input_text
if input_text:
    st.write(chain.invoke({'question':input_text}))
