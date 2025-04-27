from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()

from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_nvidia_ai_endpoints import ChatNVIDIA

loader = TextLoader(r"C:\Users\Administrator\OneDrive\Desktop\LangChainMastery\Books\state_of_the_union.txt",encoding='utf-8')
documents =  loader.load()


text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

retriever = FAISS.from_documents(texts, NVIDIAEmbeddings()).as_retriever()

docs = retriever.invoke("What did the president say about Ketanji Brown Jackson")


#print(docs)

# adding contextual compression retriever

llm = ChatNVIDIA(model='meta/llama-3.1-70b-instruct')
compressor = LLMChainExtractor.from_llm(llm)

compression_retriver = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever,
    
)

compresed_docs = compression_retriver.invoke("What did the president say about Ketanji Brown Jackson")
print(compresed_docs)