from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

#openaiembedding - to get the embeddings of the text(embedding - convert text to vectors)
embedding = OpenAIEmbeddings(model = 'text-embedding-3-large',dimension = 32)

# Embed the query i.e convert the text to vectors(multiple queries)
document = [
    "Delhi is the capital of India.",
    "India is a country in South Asia.",
    "The population of India is 1.3 billion people."
]

# Embed the document i.e convert the text to vectors
result = embedding.embed_documents(document)

print(result)