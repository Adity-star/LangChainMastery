# prefer openai if you have the api key
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat_v1.0",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    template='write a well structured and detailed report on {topic}',
    input_variables=['topic']
)

template_2=PromptTemplate(
    templte='write a 5 line summary on following text. /n{text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template | model | parser | template_2 | model | parser

result = chain.invoke({'topic':'Quantum physics'})

print(result)