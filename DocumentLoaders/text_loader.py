from langchain_community.document_loaders import TextLoader
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatNVIDIA(
    model="meta/llama-3.1-70b-instruct",
    temperature=0.1,
    max_tokens=2000,
)

prompt = PromptTemplate(
    template='Write a summary for the following text',
    input_variables=["text"],
    output_parser=StrOutputParser(),
)

loader = TextLoader(r"C:\Users\Administrator\Downloads\Text summarization.txt",encoding="utf-8")

docs = loader.load()

print(type(docs))
print('-'*25)

print(len(docs))
print('-'*25)

print(docs[0].page_content)
print('-'*25)


print(docs[0].metadata)
print('-'*25)


chain = prompt | model 

print(chain.invoke({'text':docs[0].page_content}))