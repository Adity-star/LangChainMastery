from langchain.retrievers import ParentDocumentRetriever

from langchain.storage import InMemoryStore
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()


loaders = PyPDFLoader(r"C:\Users\Administrator\OneDrive\Desktop\LangChainMastery\Books\machine-learning-roadmap.pdf")

docs = loaders.load()

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)

vectstore = Chroma(
    collection_name="test",
    embedding_function=NVIDIAEmbeddings(),
)

# Store the documents in memory
store = InMemoryStore()
retriever = ParentDocumentRetriever(
    vectorstore=vectstore,
    docstore=store,
    child_splitter=text_splitter,
)

# Add the documents to the vectorstore
retriever.add_documents(docs)

#print(list(store.yield_keys()))

# Retrieve the parent document
sub_docs = vectstore.similarity_search("Give me the roadmap for machine learning")

print(sub_docs[0].page_content)
