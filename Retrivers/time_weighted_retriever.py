# semantic_similarity + (1.0 - decay_rate) ^ hours_passed

from datetime import datetime, timedelta

import faiss
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from langchain_community.docstore import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from dotenv import load_dotenv
load_dotenv()

# Low decay rate(memory will be retained for a long time)
llm = NVIDIAEmbeddings()

size = 1024

index = faiss.IndexFlatL2(size)
vectstore = FAISS(
    index=index,
    embedding_function=llm,
    docstore=InMemoryDocstore({}),
    index_to_docstore_id={}

)

retriever = TimeWeightedVectorStoreRetriever(
    vectorstore=vectstore,
    decay_rate=0.0000000000000000000000001,
    k=1
)

yesterday = datetime.now() - timedelta(days=1)
retriever.add_documents(
    [
        Document(
            page_content="This is a test document",
            metadata={"source": "test", "timestamp": yesterday}
        )
    ]
        )

retriever.add_documents([Document(page_content='hello foo')])

result = retriever.invoke("hello world")
print(result)
print("-"*50)
