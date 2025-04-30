from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# Load environment variables (e.g., HuggingFace token)
load_dotenv()

# Set up the HuggingFace model (Gemma-2B from Google)
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)


# Wrap the model with LangChain's Chat interface
model = ChatHuggingFace(llm=llm)


# Define the schema: What fields we expect in the output and their descriptions
schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]


# Create a structured output parser that expects the LLM to return the data in this schema
parser = StructuredOutputParser.from_response_schemas(schema)


# Define the prompt template
template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


# Chain the components together: prompt → model → parser
chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)