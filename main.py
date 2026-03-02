from dotenv import load_dotenv
load_dotenv()
import os
from backend.workflow.orchestrator import create_graph
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Load environment variables from .env file

def main():
    print(f"{os.getenv('MODEL')}")
    print("Hello from ai-agent!")
    initial_input = {"messages": HumanMessage(content="can I ask for vacations")}
    # Thread
    thread = {"configurable": {"thread_id": "1"}}
    graph = create_graph(12)
    # Run the graph until the first interruption
    for event in graph.stream(initial_input, thread, stream_mode="values"):
        event['messages'][-1].pretty_print()

if __name__ == "__main__":
    main()
