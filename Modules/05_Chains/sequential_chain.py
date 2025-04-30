from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt_1 = PromptTemplate(
    template = 'Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt_2 = PromptTemplate(
    template='Generate a five line summary from following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

# sequential chain

chain = prompt_1 |  model | parser | prompt_2 | model | parser

result = chain.invoke({'topic': 'quantum physics'})

print(result)

# visualise the chain
chain.get_graph().print_ascii()