from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import joblib
import os
import random

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Load model and vectorizer
model_path = os.path.join("model", "chatbot_model.pkl")
vectorizer_path = os.path.join("model", "vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# AI Agent Names
agent_names = ["Nova", "Athena", "Zeno", "Lyra", "Echo", "Orion", "Navi", "Iris", "Vega", "Elara"]
current_agent = random.choice(agent_names)

# Route to serve the HTML UI
@app.route("/")
def index():
    return render_template("index.html")

# Serve static files like CSS, JS
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

# Chatbot welcome message
@app.route("/start", methods=["GET"])
def start_bot():
    global current_agent
    current_agent = random.choice(agent_names)
    welcome = f"👋 Welcome to RaiseHigh Tech! I'm {current_agent}, your AI assistant. How can I assist you today?"
    return jsonify({"response": welcome})

# Chatbot message response
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"response": "Invalid request"}), 400

    message = data["message"].strip()
    input_vector = vectorizer.transform([message])
    predicted_response = model.predict(input_vector)[0]

    return jsonify({"response": predicted_response})

# Favicon handler
@app.route("/favicon.ico")
def favicon():
    return '', 204

if __name__ == "__main__":
    print("🔥 Starting RaiseHigh Chatbot with UI...")
    app.run(debug=True, host="0.0.0.0", port=5000)
