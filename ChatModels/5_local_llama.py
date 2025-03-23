from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# For Langmith tracking and debugging purpose (langchain tracing)
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY") # API key for langchain

# Create a prompt for chatbot(what chatbot should say when it starts and what user should say)
prompt = ChatPromptTemplate.from_messages(
    [
        ('system','you are a chatbot.Please chat with me.'),
        ('user','Question:{question}')
    ]
)

# streamlit app framework
st.title('Langchain with Llama2')
input_text = st.text_input('Enter your question here:')

# ollama LLAma2 model which is running locally in the system(before running this code,make sure to download model in system)
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

# If input_text is not empty, invoke the model with input_text
if input_text:
    st.write(chain.invoke({"question":input_text}))