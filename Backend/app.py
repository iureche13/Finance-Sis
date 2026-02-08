from flask import Flask, request, jsonify, render_template
from chatbot import RiskAssessmentChatbot
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

chatbot = RiskAssessmentChatbot(
    api_key="sk-ced2218389c048d8b8878325a8c1f5a2",
    risk_data_path="risk_data.json"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_msg = request.json.get("message", "")
        print(f"Received message: {user_msg}")

        reply = chatbot.ask(user_msg)
        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"reply": "Internal server error"}), 500

@app.route("/risk", methods=["GET"])
def risk():
    with open("risk_data.json", "r") as f:
        chatbot.risk_data = json.load(f)
    return jsonify({
        "risk_score": chatbot.risk_data.get("risk_score"),
        "risk_level": chatbot.risk_data.get("risk_level"),
        "summary": chatbot.risk_data.get("summary", "")
    })




if __name__ == "__main__":
    app.run(debug=True)
