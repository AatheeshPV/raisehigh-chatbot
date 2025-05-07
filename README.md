🧠 RaiseHigh Tech – AI Chatbot 🤖
Welcome to the official AI chatbot for RaiseHigh Tech, a smart virtual assistant built without using third-party APIs (like OpenAI). This AI agent is trained on a custom dataset of frequently asked client questions and supports automatic welcome messages with a randomly chosen AI assistant name at each session start.

raisehigh-chatbot/
│
├── dataset/
│   ├── faq.json                # Custom questions/answers dataset
│
├── model/
│   ├── chatbot_model.pkl       # Trained ML model
│   ├── vectorizer.pkl          # Vectorizer used for feature transformation
│
├── ui/
│   ├── index.html              # Frontend chatbot UI
│
├── chatbot_api.py              # Flask API backend
├── train_model.py              # Script to train and save the model
├── requirements.txt            # Required packages
├── README.md                   # Project documentation

⚙️ Features
✅ Custom AI chatbot with local training (no external APIs).

🤖 Welcome message with random AI assistant name on every new session.

💬 Handles client questions related to startup IT services.

🧠 Uses Machine Learning with scikit-learn for response prediction.

🌐 API built with Flask + tested with Postman or Python.

🖥️ Simple HTML UI that connects to the Flask backend.


🛠️ Setup Instructions
1. Clone the Repo

git clone https://github.com/yourusername/raisehigh-chatbot.git
cd raisehigh-chatbot

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Required Packages

pip install -r requirements.txt

Requirements.txt

Flask
Flask-Cors
scikit-learn
joblib

🧪 Train the Model
Before starting the server, you must train the model:

python train_model.py

This will generate:

	chatbot_model.pkl

	vectorizer.pkl

🚀 Run the Chatbot API

python chatbot_api.py

🧪 Testing the API in Postman
Start the Flask server

Test welcome message:

GET request to: http://127.0.0.1:5000/start

Test chat endpoint:

POST request to: http://127.0.0.1:5000/chat

Body → raw → JSON:

{
  "message": "What services do you provide?"
}

🧠 Example Questions in Dataset
What services do you offer?

Do you build mobile apps?

Tell me about your pricing.

Can I get a free quote?

What technologies do you use?

Do you offer AI development?

Can I see your portfolio?

Do you offer support after deployment?

What is your project timeline?

How do I contact your team?

