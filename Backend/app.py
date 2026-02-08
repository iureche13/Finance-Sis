from flask import Flask, request, jsonify, render_template
from chatbot import RiskAssessmentChatbot
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

chatbot = RiskAssessmentChatbot(
    api_key="",
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

if __name__ == "__main__":
    app.run(debug=True)
