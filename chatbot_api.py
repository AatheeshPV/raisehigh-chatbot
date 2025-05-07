from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model_path = os.path.join("model", "chatbot_model.pkl")
vectorizer_path = os.path.join("model", "vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# AI Agent Names
agent_names = ["Nova", "Athena", "Zeno", "Lyra", "Echo", "Orion", "Navi", "Iris", "Vega", "Elara"]
current_agent = random.choice(agent_names)

@app.route("/start", methods=["GET"])
def start_bot():
    global current_agent
    current_agent = random.choice(agent_names)
    welcome = f"👋 Welcome to RaiseHigh Tech! I'm {current_agent}, your AI assistant. How can I assist you today?"
    return jsonify({"response": welcome})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"response": "Invalid request"}), 400

    message = data["message"].strip()
    input_vector = vectorizer.transform([message])
    predicted_response = model.predict(input_vector)[0]

    return jsonify({"response": predicted_response})

@app.route("/", methods=["GET"])
def index():
    return "✅ RaiseHigh Chatbot API is Running!"

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == "__main__":
    print("🔥 Starting RaiseHigh Tech AI Chatbot API...")
    app.run(debug=True, host='0.0.0.0', port=5000)
