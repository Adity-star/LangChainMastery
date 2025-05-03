# 📦 Module 03: Prompts

Welcome to Module 03 of the LangChain Mastery course! In this module, you’ll explore how to guide model behavior effectively using **Prompt Templates**. Prompt engineering is a foundational skill when working with LLMs and Chat Models — and LangChain provides powerful abstractions to make this process clean, dynamic, and reusable.

---

## 📚 What You'll Learn

- The fundamental concepts of **Prompt Templates** in LangChain
- How to use **String-based Prompt Templates** and **Chat-based Prompt Templates**
- The art of **Few-shot Prompting** for improved model performance
- How to create **Dynamic Few-shot Prompts** with **Vectorstores** and **Semantic Similarity**
- Hands-on practice with **notebooks** and examples to help you master prompt engineering


---

### 📝 What Are Prompts?
A Prompt is like a command you give to a language model to guide its behavior and generate a response. The goal of using prompts is to provide the model with clear instructions, context, and any relevant information needed to produce the best output. The beauty of LangChain is that it lets you build flexible and reusable prompt templates that can adapt to different scenarios.

---

## 🧩 Prompt Templates
LangChain provides a powerful system for creating Prompt Templates, which are pre-defined structures you can fill with dynamic content. These templates help you control the structure of your prompt, making it easier to format inputs and outputs.

### 1. [StringPromptTemplate](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/03_prompts/01_Prompt_Templates.ipynb)

- A `StringPromptTemplate` is great for creating a single prompt that can be filled with variables.
- Perfect for simple use cases where you want to format a single string and pass it to the model.
- Example use case:
  ```python
  from langchain.prompts import PromptTemplate

  prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
  prompt.format(product="colorful socks")
  ```
  Here, `{product}` is replaced by the variable `"colorful socks"`, and the final prompt becomes: "What is a good name for a company that makes colorful socks?"


### 2. [ChatPromptTemplate](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/03_prompts/01_Prompt_Templates.ipynb)
- ChatPromptTemplates are used to format a list of messages and are ideal for more complex interactions like multi-turn conversations (e.g., chatbots).
- These templates help structure the flow of conversation between system, user, and assistant roles.
Example use case:
```python
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Translate this sentence: {sentence}")
])

chat_prompt.format_messages(sentence="Bonjour le monde")
```
This generates a structured chat prompt where the model can handle the system and user messages separately.

### 3. [MessagesPlaceholder](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/03_prompts/01_Prompt_Templates.ipynb)
- MessagesPlaceholder allows you to slot in a dynamic list of messages. It’s useful when you want to pass in a list of messages (e.g., conversation history) dynamically.
- This is perfect when building chatbots or applications that need to maintain context.
Example:
```python
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "What's the next step?")
])
```
-  `chat_history` contains 5 messages, the final message list will include the system message, the 5 messages, and the final human message — totaling 7.

- ✅ An alternative way to accomplish similar behavior is to construct the message list manually without explicitly using MessagesPlaceholder.
---

###  [Few-Shot Prompting](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/03_prompts/02_fewshot_prompt_template.ipynb)
Few-shot prompting is a technique where you provide the model with a few examples of input-output pairs to guide its behavior. This helps the model understand the kind of responses you're expecting.

In this section, we'll explore Few-shot Prompt Templates and how you can use them to improve the accuracy and relevance of model responses.

#### Fixed Few-Shot Prompting
The simplest way to implement few-shot prompting is by using fixed examples. You hardcode a few input-output pairs into the prompt, and the model uses them as a reference to generate better responses.
Example:
```python
from langchain.prompts import FewShotPromptTemplate

few_shot_prompt = FewShotPromptTemplate(
    examples=[("Translate 'Hola' to English", "Hello"), ("Translate 'Gracias' to English", "Thank you")],
    input_variables=["sentence"],
    template="Translate {sentence} to English."
)

formatted_prompt = few_shot_prompt.format(sentence="Buenos días")
print(formatted_prompt)
```
### [Dynamic Few-Shot Prompting with Vectorstores](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/03_prompts/02_fewshot_prompt_template.ipynb)
Sometimes, it’s more effective to dynamically select examples based on the input. This is where vectorstores and semantic similarity come into play. You can use a SemanticSimilarityExampleSelector to dynamically choose the most relevant examples from a vectorstore.
Example
```python
from langchain.prompts import FewShotPromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Step 1: Create the vectorstore with your examples
examples = [
    ("Translate 'Hola' to English", "Hello"),
    ("Translate 'Gracias' to English", "Thank you"),
    ("Translate 'Buenos días' to English", "Good morning")
]
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts([e[0] for e in examples], embeddings)

# Step 2: Select the most relevant example based on the input
selector = SemanticSimilarityExampleSelector(vectorstore)
selected_example = selector.select("Translate '¿Cómo estás?' to English")

# Step 3: Format the prompt with the selected example
few_shot_prompt = FewShotPromptTemplate(
    examples=[selected_example],
    input_variables=["sentence"],
    template="Translate {sentence} to English."
)

formatted_prompt = few_shot_prompt.format(sentence="¿Cómo estás?")
print(formatted_prompt)
```
This will dynamically select the most relevant example based on semantic similarity and construct a tailored prompt for the model.

---
###  Why Prompts Matter
Prompts are essential for guiding language models. The way you structure your prompts — whether through simple string formatting, dynamic chat messages, or few-shot examples — directly impacts how well the model performs. LangChain gives you the flexibility to build prompts that are tailored to your specific needs, whether you're building a chatbot, running a semantic search, or generating creative content.


---
### Next Steps
Congratulations! You've learned how to create and use Prompt Templates, as well as how to leverage Few-Shot Prompting and Dynamic Example Selection. Now that you have a solid grasp of how prompts work in LangChain, it's time to dive into more complex workflows, like chaining prompts and integrating memory into your LangChain applications.

👉 Ready for Next Module? Head over to [**Module 04: OutPut Parsers**](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/04_Output%20Parsers)
