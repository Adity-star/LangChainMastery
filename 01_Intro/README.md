# 🌟 Module 01: Introduction to LangChain

Welcome to the first module of the LangChain Mastery course! In this module, we'll introduce you to **LangChain** and its powerful features. By the end, you'll have the skills to set up LangChain in your environment and run your very first LangChain application. Let’s dive in!

---

## 1.1 🚀 **What is LangChain?**

LangChain is an amazing framework designed to simplify the process of working with **Large Language Models (LLMs)**. If you’ve ever wondered how AI can generate text, answer questions, or help with complex tasks, LangChain is the framework that makes it possible. 

With LangChain, you can:
- **Chain together components** like models, memory, and prompts to create intelligent workflows.
- Work with **different LLM providers** (like OpenAI, Hugging Face, and others) seamlessly.
- Harness the power of **prompt engineering** to fine-tune how your model responds.
- **Integrate external tools** and APIs to build advanced AI applications.

Think of LangChain as your go-to toolkit for building powerful AI-driven applications, from simple chatbots to complex document search systems.

---

## 1.2 💡 **Why Use LangChain?**

You might be asking, "Why should I use LangChain?" Well, here are a few reasons:

- **Unified Interface**: LangChain allows you to work with different LLMs (like GPT-3, GPT-4, and more) using a single interface. No need to worry about the complexities of each provider!
- **Build AI Tools**: Whether you want to create chatbots, AI assistants, or document search systems, LangChain has the tools you need.
- **Memory Management**: Let your models remember context, which is especially useful for building chatbots or systems that need to keep track of conversations.
- **Custom Workflows**: Create multi-step processes where outputs from one model can be fed into another. This makes LangChain incredibly powerful for building complex applications.

If you're ready to create intelligent applications with LLMs, **LangChain is your framework**!

---

## 1.3 🛠 **Installing LangChain**

Before we start coding, let's get LangChain set up in your environment. Follow these easy steps to get everything installed and ready to go:

#### Step 1: Clone the Course Repository
First, grab the course files by cloning the repository:

```bash
git clone https://github.com/Adity-star/LangChainMastery.git
cd LangChainMastery
```

Step 2: Create a Virtual Environment
We recommend working in a virtual environment to keep everything neat and organized.
Run the following commands to create and activate your virtual environment:
```bash
python -m venv langchain-env
source langchain-env/bin/activate   # For Mac/Linux
.\langchain-env\Scripts\activate   # For Windows
```
Step 3: Install Dependencies
Once the virtual environment is active, install the required dependencies:
```bash
pip install -r requirements.txt
```
This will install LangChain and all the other necessary tools to help you get started.

---

## 1.4 💻 Writing Your First LangChain Application
Now, let’s jump into coding! We’ll start with a simple "Hello World" example. This application will interact with the OpenAI model and generate a response.
### Step 1: Explore the LangChain Intro Notebook
Before jumping into the code, take a moment to explore the [LangChain Intro Notebook](https://github.com/Adity-star/LangChainMastery/blob/main/Intro/Langchain_intro.ipynb). This will help you understand the core concepts and components of LangChain, which will be useful as you proceed with your coding exercises.
### Step 2: Create a File Called `hello_world.py`
Next, create a file named [`hello_world.py`](https://github.com/Adity-star/LangChainMastery/blob/main/Intro/hello_world.py) and add the code to interact with the OpenAI model.

---

## 1.5 🏃‍♂️ Running Your First Script
Once you've saved the file, it’s time to run the script!

In your terminal, run:
To run the script, execute the following command in your terminal:
```bash
python hello_world.py
```
You should see a response like this:
```bash
Hello! I'm doing great, thanks for asking. How can I assist you today?
```
## 1.6 📝 Your First Task: Customize Your Hello World
Awesome job! Now that you’ve seen your first LangChain app in action, let’s make it your own!
Task:
1. Modify the prompt to ask the AI about something you’re interested in. For example, you can ask:

   - “What is artificial intelligence?”

   - “Tell me about LangChain.”

   - “What’s the weather like in New York?”

2. Run the script again and print the response.

---

## 1.7 🔮 What’s Next?
Great job on completing the first module! You’ve learned how to set up LangChain and run your first application. 🎉

In the next module, we’ll dive deeper into LLMs (Large Language Models. You’ll learn how to use LLms in langchain.

Ready to level up? Let’s move on to [Module 02: Working with LLMs!](https://github.com/Adity-star/LangChainMastery/tree/main/02_LLMs)
