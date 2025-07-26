from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from pprint import pprint


# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")



# Define the prompt template
actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are expert AI researcher.
            Current time: {time}
            1. {first_instruction}
            2. Reflect on the reflection, **list 1-3 search queries separately** for
            researching improvements. Do not include them inside the reflections.
            """,
        ),
        MessagesPlaceholder(variable_name="message"),
        ("system", "Answer the user's question above using the required format."),
    ]
)

# Define the output schema
class Reflection(BaseModel):
    missing: str = Field(description="Critique of what is missing.")
    superflous: str = Field(description="Critique of what is superfluous.")

class AnswerQuestion(BaseModel):
    answer: str = Field(description="~260 words detailed answer to the question.")
    search_queries: List[str] = Field(
        description="1-3 search queries for researching improvements to address the critique of your current answer."
    )
    reflection: Reflection = Field(
        description="Your reflection on the initial answer."
    )

# Bind the instruction to the prompt
first_responder_prompt_template = actor_prompt_template.partial(
    first_instruction="Provide a detailed ~250 word answer."
)

# Create parser and chain
pydantic_parser = PydanticToolsParser(tools=[AnswerQuestion])
first_responder_chain = (
    first_responder_prompt_template
    | llm.bind_tools(tools=[AnswerQuestion], tool_choice="AnswerQuestion")
    | pydantic_parser
)

# Invoke the chain with user input and current time
response = first_responder_chain.invoke({
    "message": [HumanMessage(content="write me a blog post on how freelancer can get a job in ai industry")],
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
})

# Print the structured output
pprint(response[0].model_dump(), indent=2)
