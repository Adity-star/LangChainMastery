# Module 06: Document Loaders in LangChain

Welcome to **Module 06 – Document Loaders**! In this module, you will explore one of the most essential foundations for any retrieval-augmented or document-centric application in LangChain — **Document Loaders**.

Whether you’re building a knowledge bot, a semantic search engine, or an automated Q&A system, loading and structuring your documents correctly is crucial to success.

---

##  Why Use Document Loaders?

LangChain’s document loaders are designed to **ingest raw content** from different sources and **normalize it** into a consistent format (`Document` objects). These objects can then be:
- Indexed into vector databases
- Parsed and split into chunks for context-aware embeddings
- Queried via chains or agents for downstream NLP tasks

> Without document loaders, you'd need to manually parse and process each data format — an inefficient and error-prone task.
> 

  ---
  ## 🧰 Common Document Loaders and Their Use Cases

| Loader | Description | Use Case |
|--------|-------------|----------|
| `PyPDFLoader` | Loads content from PDF files | Reading research papers, manuals |
| `TextLoader` | Loads content from `.txt` files | Loading plain text or logs |
| `CSVLoader` | Loads data from CSV files | Structured data, tables |
| `WebBaseLoader` | Scrapes and loads content from URLs | Websites, blogs, online articles |
| `UnstructuredHTMLLoader` | Parses raw HTML with structure | Scraping structured web content |
| `DirectoryLoader` | Loads all files from a directory | Batch-processing files |
| `UnstructuredEPubLoader` | Loads `.epub` ebook files | Books, EPUB-based docs |
| `UnstructuredWordDocumentLoader` | Loads Microsoft Word `.docx` files | Business docs, contracts |
| `NotionDBLoader` | Loads data from Notion workspace | Notion content integration |
| `EmailLoader` | Parses `.eml` files | Email content processing |
| `JSONLoader` | Loads JSON content | APIs, config files, structured data |
| `MarkdownLoader` | Loads `.md` files | Blog posts, documentation |


> For Detaild hands on go through these notebooke:
> 1. [Document Loader 1](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/06_Document%20Loaders/Document_Loader.ipynb)
> 2. [Document Loader 2](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/06_Document%20Loaders/Document_Loaders_2.ipynb)
---
# Integration Strategies

Document loaders can be paired with various LangChain chains and tools:

##  With RetrievalQA Chain
**Flow**: Load → Split → Embed → Retrieve → Answer

*Ideal for document search, compliance tools, policy Q&A*

---

##  With ConversationalRetrievalChain
Add memory + history to make multi-turn Q&A possible.

*Useful in customer support and educational bots*

---

##  With Agents
Let agents decide which document or source to use.

Combine multiple loaders to form a knowledge routing system.

---

##  With Metadata Filtering
Enrich `Document` objects with metadata (e.g., title, date).

Filter documents during retrieval based on metadata constraints.

---

## For Practice
Try these
- [`cvs loader`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/06_Document%20Loaders/csv_loader.py)
- [`Directory Loader`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/06_Document%20Loaders/directory_loader.py)
- [`PDF Loader`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/06_Document%20Loaders/pdf_loader.py)
- [`Text Loader`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/06_Document%20Loaders/text_loader.py)
- [`Web Based Loader`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/06_Document%20Loaders/web_based_loader.py)

  ---
## Further Resources
- [Document Loader 1 Notebook](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/06_Document%20Loaders/Document_Loader.ipynb)
- [Document Loader 2 Notebook](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/06_Document%20Loaders/Document_Loaders_2.ipynb)
- [LangChain Documentation: Loaders](https://python.langchain.com/docs/how_to/#document-loaders)

---

## Next Step
Now that you can load content from virtually any source, it's time to split your documents intelligently.


Completed Document Loaders:Lets Go to [Module 07: Text Splitters](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/07_Text%20Splitters)



