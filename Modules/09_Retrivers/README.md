# 📦 Module 09: Vector Stores & Retrievers in LangChain

Welcome to **Module 08 – Vector Stores & Retrievers!**  
This module covers two foundational components in LangChain’s ecosystem: Vector Stores (vector databases for semantic search) and Retrievers (interfaces to fetch relevant documents from vector stores). Together, they power Retrieval-Augmented Generation (RAG) workflows that enable large language models to access external knowledge efficiently.

![retriever_full_docs-e6282aafd63f69ab3fcb26b2cfc46b5c](https://github.com/user-attachments/assets/3ecaa967-ff06-4fe2-af05-f9645b04510a)

---
##  What Are Retrievers?

Retrievers are abstractions over vector stores (and other sources) that enable retrieval of relevant documents given a user query.  
Instead of directly querying the vector store, you use retrievers which can provide additional features like filtering, batching, or query rewriting.

In LangChain, retrievers are designed to fit seamlessly with **chains** and **agents**, enabling complex, retrieval-augmented NLP workflows.

---
##  Understanding Retrievers

While **Vector Stores** handle the storage and indexing of embeddings, **Retrievers** are responsible for fetching relevant documents based on a query.  
Retrievers can operate over various data sources, including vector stores, databases, and APIs, and can incorporate additional logic such as filtering, ranking, and compression to refine the retrieval process.

###  Key Characteristics of Retrievers:

- **Abstraction Layer:**  
  Retrievers provide a unified interface to various data sources, abstracting the underlying complexities.

- **Enhanced Logic:**  
  They can implement custom logic for filtering, ranking, and processing retrieved documents.

- **Integration with Chains:**  
  Retrievers seamlessly integrate with LangChain chains, enabling complex workflows that combine retrieval with language model processing.

---
## 🗂️ Types of Retrievers in LangChain

LangChain offers a variety of retrievers, each suited for different use cases:

1. **VectorStoreRetriever**  
   **Description:** Retrieves documents from a vector store based on semantic similarity to the query.  
   **Use Case:** Ideal for applications requiring semantic search capabilities.

2. **SelfQueryRetriever**  
   **Description:** Translates a natural language query into a structured query to retrieve documents from a vector store.  
   **Use Case:** Useful when dealing with structured data or when the query needs to be interpreted in a specific context.

3. **TimeWeightedRetriever**  
   **Description:** Combines semantic similarity with a time decay factor to prioritize more recent documents.  
   **Use Case:** Suitable for applications where the recency of information is crucial, such as news aggregation.

4. **MultiVectorRetriever**  
   **Description:** Retrieves documents using multiple embeddings for the same document, such as embeddings for different sections or summaries.  
   **Use Case:** Beneficial for documents with multiple components or perspectives.

5. **ParentDocumentRetriever**  
   **Description:** Retrieves smaller chunks of a document and then fetches the larger parent document.  
   **Use Case:** Ideal for applications requiring context from the entire document after retrieving relevant chunks.

6. **ContextualCompressionRetriever**  
   **Description:** Compresses the retrieved documents using the context of the query to return only the most relevant information.  
   **Use Case:** Useful for summarizing or condensing information before presenting it to the us
---

##  Why Use Vector Stores & Retrievers?

- **Semantic Search:**  
  Find relevant documents based on conceptual meaning, not just keyword matches.

- **Efficient Large-Scale Search:**  
  Handle millions of documents with optimized nearest neighbor search algorithms.

- **Modular Design:**  
  Decouple embedding creation, storage, and retrieval for flexibility and scalability.

- **Enhanced Contextual QA:**  
  Retrieve context to ground LLM responses in external knowledge.

- **Dynamic Filtering:**  
  Narrow down search results with metadata or similarity thresholds.

---

## 🧠 Advanced Retriever Techniques

LangChain provides several advanced retriever techniques to enhance the retrieval process:

1. **Document Compression**  
   **Description:** Compresses retrieved documents to reduce their size while retaining essential information.  
   **Classes:** `ContextualCompressionRetriever`, `LLMChainExtractor`, `LLMChainFilter`, `EmbeddingsFilter`.  
   **Use Case:** Useful for improving performance and relevance in retrieval-augmented generation tasks.

2. **Ensemble Retrieval**  
   **Description:** Combines multiple retrievers to improve the diversity and quality of retrieved documents.  
   **Class:** `EnsembleRetriever`.  
   **Use Case:** Beneficial when different retrievers have strengths in different areas.

3. **Multi-Query Retrieval**  
   **Description:** Generates multiple queries from a single user query and retrieves documents for each.  
   **Class:** `MultiQueryRetriever`.  
   **Use Case:** Suitable for exploring different facets of a user's query.

4. **Rephrasing Queries**  
   **Description:** Rephrases a user's query to improve retrieval effectiveness.  
   **Class:** `RePhraseQueryRetriever`.  
   **Use Case:** Helpful when dealing with ambiguous or complex queries.

---

## Summary Table

| Retriever Type                     | Description                                                 | Use Case                                     |
| ---------------------------------- | ----------------------------------------------------------- | -------------------------------------------- |
| **VectorStoreRetriever**           | Retrieves documents based on semantic similarity            | General semantic search                      |
| **SelfQueryRetriever**             | Translates natural language queries into structured queries | Structured data retrieval                    |
| **TimeWeightedRetriever**          | Combines semantic similarity with time decay                | Prioritizing recent information              |
| **MultiVectorRetriever**           | Retrieves documents using multiple embeddings               | Documents with multiple components           |
| **ParentDocumentRetriever**        | Retrieves smaller chunks and then the parent document       | Contextual understanding of entire documents |
| **ContextualCompressionRetriever** | Compresses retrieved documents using query context          | Summarizing or condensing information        |

---
## Practice
Try this retrievers:
- [`Self Query retriver`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/09_Retrivers/self_query_retriver.py)
- [`VectorStore Retriver`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/09_Retrivers/vector_store_retriver.py)
- [`Contextual Compression retriver`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/09_Retrivers/contextual_compression_retriver.py)
- [`Parent Document Retriver`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/09_Retrivers/parent_document_retriever.py)
- [`Time Weighted Retriver`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/09_Retrivers/time_weighted_retriever.py)
- [`Multi Query retriver`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/09_Retrivers/multi_query_retriver.py)
  
## Further Reading

- [LangChain Retrievers Documentation](https://python.langchain.com/docs/concepts/retrievers/)

## Next Step
Now you are ready to build your own RAG system.You have all the knowledge required for this.
👉 [Go To Module 10: RAG](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/10_RAG)
