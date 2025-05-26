from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\Users\Administrator\OneDrive\Desktop\LangChainMastery\Books\Attention Is All You Need  by Ashish Vaswani .pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0,
    separator = ""
)

result = splitter.split_documents(docs)

print(result[0].page_content)