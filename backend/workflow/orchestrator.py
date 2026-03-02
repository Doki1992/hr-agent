from IPython.display import Image, display
# from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import MessagesState
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from backend.llm_clients.clients import llm_with_tools, tools
from langgraph.checkpoint.sqlite import SqliteSaver
from backend.utils.prompts import PROMPT
from backend.memory.messages import conn

def create_graph(employee_id: int):
    # System message
    sys_msg = SystemMessage(content=f"{PROMPT} {employee_id}")
    memory = SqliteSaver(conn)
    # Node
    def assistant(state: MessagesState):
        print(state["messages"])
        return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

    # Graph
    builder = StateGraph(MessagesState)

    # Define nodes: these do the work
    builder.add_node("assistant", assistant)
    builder.add_node("tools", ToolNode(tools))

    # Define edges: these determine the control flow
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant",
        # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
        # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
        tools_condition,
    )
    builder.add_edge("tools", "assistant")
    config = {"configurable": {"thread_id": "1"}}
   
    # memory = MemorySaver()
    graph = builder.compile(checkpointer=memory)
    graph_state = graph.get_state(config)
    return graph
    # Show
    # display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
    