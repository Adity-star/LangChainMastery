from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\Administrator\Downloads\Attention Is All You Need  by Ashish Vaswani .pdf')

docs = loader.load()

#print(docs)
print(len(docs))
print(docs[0].page_content[:1000])
print(docs[0].metadata)