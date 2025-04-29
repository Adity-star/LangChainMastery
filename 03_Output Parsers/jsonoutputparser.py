# prefer openai if you have the api key
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Load environment variables from .env (in case you're using HuggingFace API tokens)
load_dotenv()

# Define the HuggingFace model endpoint
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat_v1.0",
    task='text-generation'
)

# Wrap the HuggingFace model into LangChain's Chat interface
model = ChatHuggingFace(llm=llm)

# Create a JSON output parser to ensure the output follows a JSON format
parser = JsonOutputParser()


# PromptTemplate to ask for celebrity details and enforce a structured JSON format
template = PromptTemplate(
    template="Give me the name ,profession,age,net income of celebratie \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# Create the chain: prompt → model → parse JSON
chain = template | model | parser


result = chain.invoke({})  # Nothing to pass since prompt takes no input variables

print(result)