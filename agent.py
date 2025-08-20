##this is for 
#importing libraires
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import END,START
from langgraph.graph.state import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_PROJECT"]="TestProject"
##initializing the llm
from langchain.chat_models import init_chat_model
llm=init_chat_model("groq:llama3-8b-8192")
##llm with tool 
class State(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]
    
def make_tool_graph():
    from langchain_core.tools import tool
    @tool
    def add(a:float,b:float):
        """Adds two numbers."""
        return a + b

    tools=[add]
    tool_node=ToolNode([add])

    ##binding llm with tools
    llm_with_tool=llm.bind_functions([add])

    def call_llm_model(state:State):
        return {"messages":[llm_with_tool.invoke(state["messages"])]}
    ##creating the builder
    
    builder=StateGraph(State)
    builder.add_node("tool_calling_llm",call_llm_model) ##1. tool name,def
    builder.add_node("tools",ToolNode(tools)) ##2. tool name,def
    builder.add_edge(START,"tool_calling_llm")
    builder.add_conditional_edges(
        "tool_calling_llm", 
        tools_condition  
    )
    builder.add_edge("tools",END)
    ##compile the graph
    graph=builder.compile()
    return graph


tool_agent=make_tool_graph()