# VectoreDB

from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings # You can use any embeddings(e.g. OpenAIEmbeddings)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.retrievers import MultiQueryRetriever
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
load_dotenv()

# Load the blog posts
loader = WebBaseLoader("https://medium.com/@aakuskar.980/how-i-built-my-own-stock-server-with-python-yfinance-and-a-touch-of-nerdy-ambition-b562dc1d7b93?source=user_profile_page---------1-------------5c9ca647dacc----------------------")
docs = loader.load()


# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
texts = text_splitter.split_documents(docs)

# VectorDB
embeddings = NVIDIAEmbeddings()
vectorstore = Chroma.from_documents(texts, embeddings)

question = "how to build a stock server?"

llm = ChatNVIDIA(model='meta/llama-3.1-70b-instruct')

retriver_from_llm = MultiQueryRetriever.from_llm(
    retriever = vectorstore.as_retriever(),
    llm = llm,
)

print(retriver_from_llm.invoke(question))

