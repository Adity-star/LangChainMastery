# 📦 Module 02: Models

Welcome to **Module 02** of the LangChain Mastery course! This module focuses on working with various types of models in LangChain, including:

- 🔤 **LLMs** (Large Language Models)
- 💬 **Chat Models**
- 🧠 **Embedding Models**
You'll learn how to integrate these models with providers like **OpenAI**, **Hugging Face**, and **Cohere**, and how to use them effectively in LangChain workflows.
---

## 📚 What You'll Learn

- The difference between LLMs, Chat Models, and Embedding Models
- How to configure and run each type of model in LangChain
- Real-world use cases: from generating text to enabling semantic search
- Connecting to external providers like OpenAI, Hugging Face, and Cohere

---
## 🔧 Setup

Before running the examples, make sure to install the required dependencies:

```bash
pip install -r requirements.txt
```
Ensure you have your API keys set up for providers like OpenAI or Hugging Face in your environment variables or .env file:
```bash
OPENAI_API_KEY=your-openai-key
HUGGINGFACEHUB_API_TOKEN=your-huggingface-token
```
---

### 🔤 [LLMs (Large Language Models)](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/02_models/LLMs)
LLMs are powerful tools for generating human-like text.
In this section, you'll learn how to:
- Load and configure text completion models
- Send prompts and receive generated responses
- Use different providers like OpenAI and Hugging Face

👉 **Start here:**  
Dive into the concepts, syntax, and best practices for working with LLMs in LangChain:

🔍 [**Understanding LLMs in LangChain**](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/02_models/LLMs#-understanding-llms-in-langchain)  
This section breaks down how LangChain interfaces with LLMs, what you can control, and how different providers behave.

📁 **What's inside the folder:**

- [`llm_model.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/LLMs/llm_model.py) – Simple example using OpenAI’s text completion
- [`my_text_generator.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/LLMs/huggingface_llm.py) – Simple task for you to complete.
- 📝 Step-by-step explanation in the README to walk you through key concepts

> 💡 Tip: Try tweaking the prompt or swapping providers to see how the outputs change!

---
### 💬 [Chat Models](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/02_models/ChatModels)

Chat models are designed for interactive, multi-turn conversations. They excel in use cases like chatbots, virtual assistants, and interactive Q&A systems. This section helps you explore how to build dynamic, conversational AI using various model providers.
In this section, you'll learn how to:
-  Build chatbots using structured message passing (`system`, `user`, `assistant` roles)
-  Handle multi-turn conversations with memory and context
-  Use a variety of chat model providers, including **OpenAI**, **Hugging Face**, **Local Llama**, and **Anthropic**
-  Build a fully functioning **chatbot with a Streamlit interface** for real-time interaction


👉 **Start here:**  
Explore how LangChain makes it easy to set up and run chat models in a conversational context.

🔍 [**Understanding Chat Models in LangChain**](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/02_models/ChatModels#-understanding-chat-models-in-langchain)  
Learn how to structure and pass messages in a multi-turn conversation, and how to leverage LangChain for better conversational AI interactions.

📁 **What's inside the folder:**

- [`openai_chat_model.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/ChatModels/openai_chat_model.py) – Setting up ChatGPT (OpenAI) with LangChain
- [`huggingface_chat_model.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/ChatModels/huggingface_chat_model.py) – Integrating Hugging Face models for chatbots
- [`local_llama_chat_model.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/ChatModels/local_llama_chat_model.py) – Running Local Llama chat model
- [`anthropic_chat_model.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/ChatModels/anthropic_chat_model.py) – Chatbot example with Anthropic models
- [`streamlit_chatbot.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/ChatModels/streamlit_chatbot.py) – Creating a simple chatbot UI using Streamlit for interactive sessions

> 💡 Tip: Try out the Streamlit interface to chat with your bot in real-time and explore how different models interact with users.

---
### 🧠 [Embedding Models](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/02_models/EmbeddingModels)

Embedding models are the backbone of semantic search, document retrieval, and similarity-based tasks. By converting text into high-dimensional vectors, these models enable your AI to understand the deeper meaning of words, sentences, and documents.
In this section, you'll learn how to:
-  Generate **embeddings for queries** and **documents** using OpenAI
-  Use **Hugging Face** models to create embeddings locally
-  Implement **document similarity** for tasks like semantic search and clustering
-  Integrate embeddings with LangChain’s retriever tools for smarter document processing



👉 **Start here:**  
Explore how embeddings work and how they can be leveraged to build powerful, context-aware applications.

🔍 [**Understanding Embeddings in LangChain**](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/02_models/EmbeddingModels#-understanding-embeddings-in-langchain)  
This section explains the concept of embeddings, how they transform text into vectors, and how LangChain helps you work with these embeddings for more intelligent applications.


📁 **What's inside the folder:**

- [`openai_query_embedding.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/EmbeddingModels/openai_query_embedding.py) – Generate embeddings for queries using OpenAI’s API
- [`openai_docs_embedding.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/EmbeddingModels/openai_doc_embedding.py) – Embeddings for documents using OpenAI to power semantic search
- [`huggingface_local_embedding.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/EmbeddingModels/huggingface_local_embedding.py) – Generating local embeddings with Hugging Face
- [`doc_similarity.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/02_models/EmbeddingModels/doc_similarity.py) – Compare and measure similarity between documents using embeddings

> 💡 Tip: Play around with the **document similarity** example to see how well your model can match documents based on semantic meaning, not just keywords!

 Whether you're building a search engine, recommendation system, or RAG (retrieval-augmented generation) application, **this section gives you the tools to enable smarter, context-aware search and document handling.**

## Next Steps
In this module, you've learned how to work with LLMs, Chat Models, and Embedding Models in LangChain. 
Now that you have a solid foundation, it's time to dive deeper and learn how to fine-tune model behavior using effective prompts.

Ready to dive deeper? Head over to [**Module 03 – Prompts**](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/03_prompts)

