# LangChainMastery 

Welcome to **LangChain Mastery** – a curated, hands-on repository to help you learn LangChain from scratch to advanced use cases. Whether you're just starting out or looking to deepen your understanding of advanced LLM workflows, this repo provides structured examples, explanations, and projects to guide your journey.

## What is LangChain?

[LangChain](https://www.langchain.com/) is a powerful framework designed to simplify the development of applications using large language models (LLMs). It provides tools to chain together components like models, memory, agents, tools, and data sources into powerful AI-driven applications.

---

# ⚙️ LangChain Components

LangChain is modular by design. These components can be combined in different ways to build sophisticated LLM-powered workflows. Here's a breakdown of the key components you'll explore:


## 🧱 Modules Overview

| Module | Topic | Description |
|--------|-------|-------------|
| 01 | [Introduction to LangChain](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/01_Intro#-module-01-introduction-to-langchain) | What is LangChain, how it works, and how to set it up |
| 02 | [Using Models](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/02_models#-module-02-models) | How to use OpenAI and Hugging Face models with LangChain |
| 03 | [Prompts](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/03_prompts#-module-03-prompts) | Using prompting in LangChain effectively |
| 04 | [Output Parsers](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/04_Output%20Parsers#-module-04-output-parsers-in-langchain) | Parse and structure outputs from LLMs for better usability |
| 05 | [Chains](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/05_Chains) | Combine LLM calls into multi-step logic |
| 06 | [Document Loaders](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/06_Document%20Loaders) | Build modular and composable components with LangChain's Runnable interfaces |
| 07 | [Not Done yet](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/07_Document%20Loaders) | Load and process various types of documents for use in chains |
| 08 | [Text Splitters](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/08_Text%20Splitters) | Split large text into manageable chunks for better processing |
| 09 | [Retrievers](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/09_Retrivers) | Use embeddings and retrievers for semantic search and retrieval |
| 10 | [Retrieval-Augmented Generation (RAG)](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/10_RAG) | Combine retrieval with generation to answer queries from documents |
| 11 | [Final Projects](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/11_Projects) | Build a chatbot, PDF Q&A bot, or AI assistant with real use cases |



---
## 📘 Fundamental Concepts

Start your LangChain journey with these foundational topics, designed to help you understand core concepts through hands-on examples.

1. 📖 [**Intro to LangChain**](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/01_Intro)  
   A beginner-friendly introduction explaining:
   - What LangChain is  
   - Why it’s useful for building with LLMs  
   - How to set up and run your first LangChain application

> 🤖 **Build Your First Chatbot**  
>  - LangChain + HuggingFace to build a basic conversational agent. 
>  - Basic logic to handle input and LLM response.
>  - 📝 [Basic Chatbot (chatbot.py)](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/01_Intro/chatbot.py)

> 🧠 **Enhance Chatbot with Prompt Engineering**  
> - Controlling LLM behavior via carefully designed prompts.
> - How different phrasing influences the model’s responses.
> - ✨ [Chatbot with Prompt (prompt.py)](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/01_Intro/prompt.py)

---

2. [Models](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/02_models)

Learn how to connect LangChain with popular model providers and use different types of models in your applications:

#### 🔤 LLMs (Large Language Models)
Use text generation models to complete tasks like answering questions, summarizing, or generating content.
- Providers: OpenAI, Hugging Face, Cohere, and more  
- Learn how to integrate and configure these models in LangChain

> 🔗 **Simple LLM with OpenAI**  
> A practical example showing how to use OpenAI's models with LangChain.  
> 📄 [View Code: `llm_model.py`](https://github.com/Adity-star/LangChainMastery/blob/main/02_LLMs/llm_model.py)


#### 💬 [Chat Models](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/02_models/ChatModels)
Designed for conversational use cases (like ChatGPT), these models allow message-based interactions.
- Handle structured dialogues with roles (`user`, `assistant`, etc.)
- Use tools like `ChatOpenAI` for better control and reliability


#### 🧠 [Embedding Models](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/02_models/EmbeddingModels)
Convert text into high-dimensional vectors for tasks like:
- Semantic search
- Similarity comparison
- Retrieval-augmented generation (RAG)

> 🔍 Power your retrievers with vector embeddings for smarter, context-aware applications.
---
3. [📝 Prompts](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/03_prompts)
Learn how to design effective prompts for different tasks and control LLM behavior. This section covers:
- Basic prompt construction principles
- Techniques to guide model outputs
- How to optimize prompts for specific applications
> ✨ Prompt Design Strategies
> How to make LLMs respond to user inputs more effectively
> Using different prompt patterns to influence model responses.
> - [Prompt Templates](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/03_prompts/01_Prompt_Templates.ipynb)
> - [Few Shot Prompt Templates](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/03_prompts/02_fewshot_prompt_template.ipynb)

---
4. 🧾 [Output Parsers](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/04_Output%20Parsers)
   
Learn how to extract structured data from raw LLM outputs using output parsers. This module covers:
- Why output parsing is important
- Different parser types in LangChain
- How to convert free-form text into usable formats like JSON or lists
> 🧪 Practical Parsing Examples
> See how to use built-in parsers to format and structure model outputs effectively:
> 📄 [Explore Output Parsers](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/04_Output%20Parsers#-module-03-output-parsers-in-langchain)


---

5. [🔗 Chains](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/05_Chains#-module-04-chains-in-langchain)

Chains let you build workflows by combining prompts, models, retrievers, and logic steps — allowing for more advanced LLM applications.

This module covers:
- How to structure multi-step workflows using LangChain’s `Chain` classes
- Key patterns like `SequentialChain`, `ParallelChain`, `ConditionalChain`, and `RetrievalQA`
- Using memory and external data with `ConversationalRetrievalChain`

