import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.Graph import graph

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Research Agent is Live 🚀"
    })


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "Request body must be JSON"
            }), 400

        question = data.get("question")

        if not question:
            return jsonify({
                "status": "error",
                "message": "Question is required"
            }), 400

        # Initial state for LangGraph
        initial_state = {
            "query": question,
            "search_results": [],
            "webpages": [],
            "notes": [],
            "report": ""
        }

        # Run Research Agent
        result = graph.invoke(initial_state)

        return jsonify({
            "status": "success",
            "question": question,
            "response": result["report"]
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )