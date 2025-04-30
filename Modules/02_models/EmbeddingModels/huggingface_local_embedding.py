from langchain_huggingface import HuggingFaceEmbeddings

# embedding with huggingface model - open source model
embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of India."

result = embedding.embed_query(text)

print(result)