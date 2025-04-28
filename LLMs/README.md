## 🤖 Understanding LLMs in LangChain

Large Language Models (LLMs) are the core engines behind modern AI applications such as chatbots, summarizers, translators, and code assistants. In LangChain, LLMs are modular and plug-and-play components that take a string as **input** and return a string as **output** — making them easy to use in a wide range of applications.

LangChain itself doesn’t host LLMs. Instead, it provides a **standardized interface** to interact with models from different providers, abstracting away the complexities of each underlying API.

### 🌐 Supported LLM Providers
LangChain integrates smoothly with several major LLM platforms, including:
- **OpenAI** (e.g., GPT-4, GPT-3.5)
- **Hugging Face Transformers**
- **Anthropic Claude**
- **Cohere**
- **Google PaLM** (via Vertex AI)
- And many more...

  ---

### ⚙️ How LangChain Uses LLMs

LangChain wraps each LLM behind a common interface, allowing you to:

- ✅ Generate responses based on natural language prompts  
- 🧠 Combine models with memory to hold conversational context  
- 🧩 Use prompt templates for better control over responses  
- 🔗 Chain outputs across multiple steps in a workflow  
- 🤖 Power agents that can use tools, browse, or query databases
---
  

### 🧪 Hands-On: Using an OpenAI LLM

In the following example, you'll learn how to use OpenAI’s models with LangChain. You'll configure the model, pass prompts, and receive completions using LangChain’s built-in wrappers.

🔍 **Explore the code example here:**  
👉 [LLM Example with OpenAI (`llm_model.py`)](https://github.com/Adity-star/LangChainMastery/blob/main/LLMs/llm_model.py)
