from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage
from langchain.chains import LLMChain, ConversationChain
from langchain.embeddings import OpenAIEmbeddings, GooglePalmEmbeddings
from langchain.vectorstores import SupabaseVectorStore
from langchain.chat_models import ChatOpenAI
from langchain.memory import SQLiteEntityStore
from langchain.agents import initialize_agent, AgentType, Tool, load_tools, Agent

import os

openai_api_key = os.environ.get("OPENAI_API_KEY")

gpt3 = ChatOpenAI(
    openai_api_key = openai_api_key,
    model = "gpt-3.5-turbo-16k",
    temperature = 0.5,
    presence_penalty = 0.75,
    frequency_penalty = 0.5
)

gpt4 = ChatOpenAI(
    openai_api_key = openai_api_key,
    model = "gpt-4",
    temperature = 0.5,
    presence_penalty = 0.75,
    frequency_penalty = 0.5
)

assistant_sys_msg_content = """You are a friendly, generally pleasant, AI assistant named "Luna" who strives to assist 
users to the best of your ability. Your generally pleasant demeanor should be calm and reflective, but also extremely 
pragmatic. Think a female version of the character Jonah from Bojack Horseman. He is the perfect example of the 
demeanor and pragmatic assistant that you should strive to be.

You are going to be assisting a 4th grade elementary school teacher at Churchville Chili Elementary School in Chili, NY.
Please provide general assistance appropriate for a 27 year old, female, stereotypical teacher. Fortunately, you happen
to be an expert in human psychology generally, but with a strong focus on childhood behavioral psychology, childhood 
education, and the generally accepted, scientifically backed, best practices for teaching children. That's why you were
chosen for this role!"""
#Build out the general assistant framework
assistant_sys_msg = SystemMessage(content = assistant_sys_msg_content)

conv_chain = ConversationChain()
tool_names = ["google_search", "wikipedia","youtube","office365", "file_management", "gmail"]
tools = load_tools(tool_names)

agent = initialize_agent(
    tools = tools,
    llm = gpt4,
    agent = AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
)

class Assistant:
    gpt4 = gpt4
    agent = agent
    memory = SQLiteEntityStore(
        session_id = "assistant",
        db_file = "assistant_chat.db",
    )
    def __init__(self, gpt4, agent, memory):
        self.gpt4 = gpt4
        self.agent = agent
        self.memory = memory

    def agent_help(self, input:str):
        agent_input = input("How can I help you?")
        help = self.agent.run(agent_input)

        return help