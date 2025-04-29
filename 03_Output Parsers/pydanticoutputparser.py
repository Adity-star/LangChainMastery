from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# Define the HuggingFace LLM endpoint (using Gemma-2B model)
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

# Wrap it with LangChain's Chat interface
model = ChatHuggingFace(llm=llm)

# Define the structure of the expected output using a Pydantic model
class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')


# Create the parser that expects output in the format of the Person model
parser = PydanticOutputParser(pydantic_object=Person)


# Define the prompt, injecting format instructions from the parser
template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


# Chain the components: Prompt → Model → Parser
chain = template | model | parser

final_result = chain.invoke({'place':'sri lankan'})

print(final_result)