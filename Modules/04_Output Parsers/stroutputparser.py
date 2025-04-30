# prefer openai if you have the api key
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables (e.g., HuggingFace API key)
load_dotenv()


# Define the base LLM using a TinyLlama model hosted on HuggingFace
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat_v1.0",
    task='text-generation'
)

# Wrap the model to make it compatible with LangChain's chaining interface
model = ChatHuggingFace(llm=llm)

# Define the first prompt: generates a detailed report on the input topic
template = PromptTemplate(
    template='write a well structured and detailed report on {topic}',
    input_variables=['topic']
)

# Define the second prompt: summarizes the generated report in 5 lines
template_2 = PromptTemplate(
    template='write a 5 line summary on following text.\n{text}',
    input_variables=['text']
)


# Create a string output parser to extract plain text from model outputs
parser = StrOutputParser()


# Build a chain of components:
# 1. Insert topic into template
# 2. Pass to LLM
# 3. Parse to plain string
# 4. Insert into summary prompt
# 5. Pass to LLM again
# 6. Parse final output to string
chain = template | model | parser | template_2 | model | parser


# Run the chain with a sample input topic
result = chain.invoke({'topic':'Quantum physics'})

print(result)