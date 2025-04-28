from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# define a prompt
prompt = PromptTemplate(
    template='Generate a five line summary about topics {topic}',
    input_variables=['topic']
)

# model
model = ChatOpenAI()

parser = StrOutputParser()

#simple chain
chain = prompt | model | parser

result = chain.invoke({'topic':'quantum physics'})

print(result)