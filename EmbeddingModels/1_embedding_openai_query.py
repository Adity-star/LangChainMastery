from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

#openaiembedding - to get the embeddings of the text(embedding - convert text to vectors)
embedding = OpenAIEmbeddings(model = 'text-embedding-3-large',dimension = 32)

# Embed the query i.e convert the text to vectors
result = embedding.embed_query('Delhi is the capital of India?')

print(result)