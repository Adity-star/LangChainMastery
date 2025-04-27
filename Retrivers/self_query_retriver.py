from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = NVIDIAEmbeddings()

docs = [
    Document(
        page_content="A bunch of scientists bring back dinosaurs and mayhem breaks loose",
        metadata={"year": 1993, "rating": 7.7, "genre": "science fiction"},
    ),
    Document(
        page_content="Leo DiCaprio gets lost in a dream within a dream within a dream within a ...",
        metadata={"year": 2010, "director": "Christopher Nolan", "rating": 8.2},
    ),
    Document(
        page_content="A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea",
        metadata={"year": 2006, "director": "Satoshi Kon", "rating": 8.6},
    ),
    Document(
        page_content="A bunch of normal-sized women are supremely wholesome and some men pine after them",
        metadata={"year": 2019, "director": "Greta Gerwig", "rating": 8.3},
    ),
    Document(
        page_content="Toys come alive and have a blast doing so",
        metadata={"year": 1995, "genre": "animated"},
    ),
    Document(
        page_content="Three men walk into the Zone, three men walk out of the Zone",
        metadata={
            "year": 1979,
            "director": "Andrei Tarkovsky",
            "genre": "science fiction",
            "rating": 9.9,
        },
    ),
]
vectorstore = Chroma.from_documents(docs, embeddings)

# SelfQueryRetriever
from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_nvidia_ai_endpoints import ChatNVIDIA

# Define the attributes to query
attributes = [
    AttributeInfo(
        name="genre",
        description="The genre of the movie",
        type='string or list[string]',
    ),
    AttributeInfo(
        name="year",
        description="The year the movie was released",
        type='integer',
    ),
    AttributeInfo(
        name="rating",
        description="The rating of the movie",
        type='float',
    ),
    AttributeInfo(
        name="director",
        description="The director of the movie",
        type='string',
    ),
]
# Create the retriever
document_content_description = "Brief summary of the movie"
llm= ChatNVIDIA(model='meta/llama-3.1-70b-instruct')

retriever = SelfQueryRetriever.from_llm(
    vectorstore=vectorstore,
    llm=llm,
    document_contents=document_content_description, 
    metadata_field_info=attributes,
    verbose=True
)

result = retriever.invoke("what are some movies with dinosaurs?")
print(result)
