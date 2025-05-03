# 🔗 Module 04: Chains in LangChain

Welcome to **Module 04 – [Chains](https://python.langchain.com/docs/versions/migrating_chains/)**, where we explore one of the most powerful building blocks in LangChain. Chains allow you to **combine multiple steps into a single workflow**, enabling you to create robust, multi-part applications that go beyond just a single prompt and response.

Whether you want to summarize a document, answer user queries using retrieved context, or apply sequential logic to multiple models and tools — **Chains** are how you make it happen!

---

## 📚 What You'll Learn

- What Chains are and why they’re fundamental to LangChain
- How to use different types of chains: Simple, Sequential, Conditional, and Parallel
- How to pass data between steps and control execution flow
- Tips for chaining prompts, tools, and models together
- The difference between static chains and dynamic decision-making
---
## 🧠 What Are Chains in LangChain?
In LangChain, Chains are the foundation of creating powerful workflows and applications. They allow you to combine multiple steps into one seamless process, helping you solve complex tasks that require more than just a simple prompt-to-response interaction. Chains provide the flexibility to break down larger tasks, apply logic, and integrate different tools or models.
 a **Chain** is a pipeline that connects different components — like prompts, models, retrievers, and tools — so they work together in a defined sequence or structure. 

#### Why Use Chains?
Chains enable you to:
- **Break large problems into smaller steps**: You can decompose complex tasks into simpler, more manageable ones. Each step handles a part of the process.
- **Control and reuse logic**: Once you've defined a chain, you can reuse it across different tasks, saving time and effort in building your application.
- **Add memory, conditionals, or branching**: Chains can include memory (to track context), conditional logic (to make decisions based on input), or branching paths (to run different logic depending on conditions).
- **Run tasks in sequence or parallel**: Chains can be structured to execute one after the other (sequentially) or in parallel, depending on the requirements.

In LangChain, Chains can be as simple as a prompt + model, or as complex as multi-step pipelines involving memory, retrieval, agents, and more.
ach component in the chain can interact with others, processing the data step-by-step or performing different actions based on specific inputs.

![70f1a901-259c-4b87-a525-e35afba20461](https://github.com/user-attachments/assets/db38ff07-aa24-49aa-b7f4-876f2780867c)

---

## 🔗 Chain Types Explained

### 1.  SimpleChain
A SimpleChain in LangChain is the most basic type of chain. It consists of a single input and a single output, where the input goes through a prompt and is processed by a model (LLM), giving you a direct output. It's the simplest form of chaining when you're just working with one model and one prompt.

This type of chain is great when you just want to encapsulate a single task—like translating text, answering a question, or generating text based on a specific input. It’s a straightforward, linear workflow where one input leads to one output.
Use it when:
- You have a single task that needs to be done (like translating or answering a question).
- You are working with one model and one prompt.
- You want a clean and simple way to manage your interactions.

**Code Template**:
```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate.from_template("Translate the following to French: {text}")
llm = OpenAI()
chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run("How are you?")
print(response)
```
Visual:
```css
[ User Input ] 
     ↓
[ PromptTemplate ]
     ↓
[ OpenAI LLM ]
     ↓
[ Output ]
```

> ✅ Use when you want a clean, reusable function-like structure around a single prompt.
> - [Simple_chain.py](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/05_Chains/simple_chain.py)
---
### 2.  SequentialChain
A SequentialChain allows you to run multiple chains one after another. The output of one chain becomes the input for the next.

There are two main types:
-` SimpleSequentialChain`: Passes outputs as raw strings from one step to the next.
- `SequentialChain`: Offers more control with named input/output variables (great for advanced workflows).
- Use Case Example: Extracting keywords → Using them to generate a tweet.

```python
from langchain.chains import SimpleSequentialChain, LLMChain
from langchain.prompts import PromptTemplate

llm = OpenAI()

# Step 1: Generate a blog title
prompt1 = PromptTemplate.from_template("Write a blog title about {topic}")
chain1 = LLMChain(llm=llm, prompt=prompt1)

# Step 2: Generate an intro for that title
prompt2 = PromptTemplate.from_template("Write an intro for a blog titled: {text}")
chain2 = LLMChain(llm=llm, prompt=prompt2)

# Combine
overall_chain = SimpleSequentialChain(chains=[chain1, chain2])
response = overall_chain.run("AI in Finance")
print(response)
```
Visual:
```css
[ topic ]
   ↓
[ Chain 1: Title ]
   ↓
[ Chain 2: Intro ]
   ↓
[ Output ]
```
> [Sequential_chain.py](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/05_Chains/sequential_chain.py)
---
### 3. Conditional Chain
A `ConditionalChain` (also called a Router Chain) is a special kind of chain in LangChain that chooses a path based on the input.

Think of it like a smart decision-maker:
Depending on what the user says or asks, it decides which tool, prompt, or model to use.
It's used when 
- You have different types of prompts for different tasks.
- You want a bot that can switch skills (e.g., summarize OR translate OR generate code).
- You want to build a decision tree for conversation or workflow automation.
Code Template
```python
from langchain.chains.router import MultiRouteChain
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# Define router logic
router_prompt = PromptTemplate.from_template("Decide task type: {input}")
router_chain = LLMChain(llm=ChatOpenAI(), prompt=router_prompt)

# Define destination chains
summarize_chain = LLMChain(llm=ChatOpenAI(), prompt=PromptTemplate.from_template("Summarize: {input}"))
translate_chain = LLMChain(llm=ChatOpenAI(), prompt=PromptTemplate.from_template("Translate: {input}"))

# Combine into a MultiRouteChain
multi_route_chain = MultiRouteChain(
    router_chain=router_chain,
    destination_chains={
        "summarize": summarize_chain,
        "translate": translate_chain,
    },
    default_chain=summarize_chain  # fallback
)

# Run the chain
response = multi_route_chain.run("Translate this to French: Hello, how are you?")
```
> [conditional_chain.py](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/05_Chains/conditional_chain.py): This is where LangChain defines logic for routing between chains based on conditions.

---

### 4.  RetrievalQA Chain
Retrieval-based chains let you pull in external knowledge (e.g., documents or vector databases) and use it as part of your prompt.
- Combine a retriever with a language model
- Useful for building question-answering systems or RAG applications
Code Template:
```python
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI

retriever = FAISS.load_local("your_faiss_index", OpenAIEmbeddings()).as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)

answer = qa_chain.run("What is LangChain?")
print(answer)
```
> Perfect for building knowledge-based bots and document Q&A systems.
Visual:
```css
[ User Question ]
       ↓
[ Retriever pulls relevant docs ]
       ↓
[ Prompt + Context → LLM ]
       ↓
[ Answer ]
```

---
### 5. Parallel chain
A **ParallelChain** in LangChain is designed to run multiple chains simultaneously (in parallel), and then merge the results into a single output. This is extremely useful when you want to perform multiple tasks at once and aggregate the results afterward.
Use it when:
- You need to extract multiple outputs simultaneously from different chains.
- You want to perform parallel processing tasks like generating summary, keywords, and tone analysis of a document all at once.
- You aim to improve efficiency by running tasks concurrently instead of sequentially.


```css
Input
 ├──▶ Chain A
 ├──▶ Chain B
 └──▶ Chain C
       ↓
  [ Combine Outputs ]
```

> [Parallel Chain.py](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/05_Chains/parallel_chain.py)
---
 
### 6.  ConversationalRetrievalChain (with Memory)
This advanced chain:

-  relevant context
- Maintains conversation history via memory
- Useful for building chatbots that remember

Components Involved:
- LLM
- Retriever
- PromptTemplate

Memory (like ConversationBufferMemory)
Code Template:
```python
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

llm = OpenAI()
retriever = FAISS.load_local("your_index", OpenAIEmbeddings()).as_retriever()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

response = chain.run({"question": "What is LangChain?", "chat_history": []})
print(response)
```
Visual:
```css
[ User Input + Chat History ]
           ↓
[ Retriever + Memory ]
           ↓
[ Prompt + Context → LLM ]
           ↓
[ Response (aware of history) ]
```

> Adds persistent context so your bot doesn't forget previous turns.

---
# 🧰 **Summary Table**

| Chain Type                    | Purpose                                    | Memory | Retrieval | Sequential   |
|---------------------------------|--------------------------------------------|--------|-----------|--------------|
| **LLMChain**                    | Single-step LLM call                       | ❌     | ❌        | ❌           |
| **SimpleSequentialChain**       | Linear flow of LLMChains                   | ❌     | ❌        | ✅           |
| **SequentialChain**             | Multi-step logic with variable passing     | ❌     | ❌        | ✅           |
| **ConditionalChain**            | Branching logic                            | ❌     | ❌        | ⚠️ Dynamic   |
| **ParallelChain**               | Multiple chains run simultaneously         | ❌     | ❌        | 🚀 Parallel  |
| **RetrievalQA**                 | QA from documents                          | ❌     | ✅        | ❌           |
| **ConversationalRetrievalChain**| Chat + memory + retrieval                  | ✅     | ✅        | ✅           |

---

# Practice with these chain examples 
| File | Description |
|------|-------------|
| [`simple_chain.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/05_Chains/simple_chain.py) | A minimal working example using one LLM and prompt |
| [`sequential_chain.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/05_Chains/sequential_chain.py) | A chain that performs multi-step processing (e.g. summarization → translation) |
| [`conditional_chain.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/05_Chains/conditional_chain.py) | Implements branching logic based on inputs |
| [`parallel_chain.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/05_Chains/parallel_chain.py) | Runs multiple chains side-by-side and merges their outputs |

---
### Try It Yourself!
You can experiment by:
- Swapping in different LLM providers (e.g., Hugging Face, Cohere)
- Changing prompts to alter the behavior of your chain
- Adding memory to Sequential or Retrieval chains

---

### Why Use Chains?
Chains unlock the full power of LangChain. They allow you to:
- Keep logic modular and maintainable
- Reuse components like prompts and models
- Scale your applications with cleaner architecture

Whether you're building a chatbot, document assistant, or multi-step agent, Chains help you go from idea to production-ready logic.

---
### Next Steps
Once you’ve mastered **Chains**, you’re ready to explore Agents — dynamic systems that decide what to do next based on user input and context.

👉 Finally copleted chains,ready for next ?Lets go to [Module 06: Document Loaders](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/07_Document%20Loaders)

