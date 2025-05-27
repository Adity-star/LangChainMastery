from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, tool
from langchain_community.tools import TavilySearchResults
import datetime
load_dotenv()

search_tool = TavilySearchResults()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

@tool
def get_date_time(format:str = "%Y-%m-%d %H:%M:%S"):
    """
    Returns the current date and time in the specified format.
    Default format is 'YYYY-MM-DD HH:MM:SS'.
    """
    return datetime.datetime.now().strftime(format)
    curr_time = datetime.datetime.now()
    formatted_time = curr_time.strftime(format)
    return formatted_time

agent = initialize_agent(tools=[search_tool,get_date_time],llm = llm, agent="zero-shot-react-description", verbose=True)


agent.invoke("when is current date and time in nework city")