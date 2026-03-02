from flask import Flask, request, jsonify
from backend.workflow.orchestrator import create_graph
from flask_cors import CORS
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")


@app.route("/healthcheck", methods=["GET"])
def init():
    return "good"

@app.route("/agent", methods=["POST"])
def chat():    
    body = request.get_json()
    print(body)
    employeed_id = body.get("employeeId")
    message = body.get("messages")
    message = message[-1]['content']
    graph = create_graph(employee_id=1234)
    thread = {"configurable": {"thread_id": "1"}}
    initial_input = { "messages": HumanMessage(content=message) }
    result = ''
    for event in graph.stream(initial_input, thread, stream_mode="values"):
        result = event['messages'][-1]
        result = result.content

    return jsonify({
        "message": result,
        "status": "success"
    }), 201
    


    

    