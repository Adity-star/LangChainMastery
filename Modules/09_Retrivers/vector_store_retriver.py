#  How to use a vectorstore as a retriever

# import 

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()
# Load the documents
loader = TextLoader(r"C:\Users\Administrator\OneDrive\Desktop\LangChainMastery\Books\Text summarization.txt")

docs = loader.load()

# Split the documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)

embeddings = NVIDIAEmbeddings()

# Create the vectorstore
vectorstore = FAISS.from_documents(texts, embeddings)

retriver = vectorstore.as_retriever()

docs = retriver.invoke("What is the summary of the text?")

print(docs)
