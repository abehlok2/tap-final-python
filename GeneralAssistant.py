from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage
from langchain.chains import LLMChain, ConversationChain
from langchain.embeddings import OpenAIEmbeddings, GooglePalmEmbeddings
from langchain.vectorstores import SupabaseVectorStore
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType, Tool, load_tools, Agent
import os
openai_api_key = os.environ.get("OPENAI_API_KEY")
gpt3 = ChatOpenAI(

    openai_api_key=openai_api_key,

    model="gpt-3.5-turbo-16k",

    temperature=0.5,

    presence_penalty=0.75,

    frequency_penalty=0.5

)

gpt4 = ChatOpenAI(

    openai_api_key=openai_api_key,

    model="gpt-4",

    temperature=0.5,

    presence_penalty=0.75,

    frequency_penalty=0.5

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

# Build out the general assistant framework

assistant_sys_msg = SystemMessage(content=assistant_sys_msg_content)

conv_chain = ConversationChain(
    llm = gpt4,
    memory = ConversationBufferMemory(),
)
tool_names = ["google-search", "wikipedia", "office365", "file-management", "gmail"]
tools = load_tools(tool_names)

agent = initialize_agent(
    tools=tools,
    llm=gpt4,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,

)


class Assistant:
    def __init__(self, agent, llm, tools):
        self.agent = agent
        self.llm = llm
        self.tools = tools
        self.memory = ConversationBufferMemory()
        self.conv_chain = ConversationChain(llm=self.llm, memory=self.memory)

    def get_agent_help(self):
        agent_input = input("How can I help you?")
        help_output = self.agent.run(agent_input)
        return help_output

    def chat_with_agent(self):
        print("How can I assist you today?")
        print('Please enter "stop" to end the conversation.')
        while True:
            user_input = input()
            if user_input.lower() == "stop":
                break
            self.memory.add_user_message(user_input)  # Update memory with user's message
            agent_output = self.agent.run(user_input)  # Get agent's response
            print(agent_output)
            conv_output = self.conv_chain(user_input)  # Generate response using conversation chain
            self.memory.add_agent_message(conv_output)  # Update memory with agent's message
            print(conv_output)


test = Assistant(
    agent=agent,
    llm=gpt4,
    tools=tools
)

test.chat_with_agent()
