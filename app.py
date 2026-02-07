from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    risk_score = data.get("risk_score", 0)
    risk_level = data.get("risk_level", "Low")
    summary = data.get("summary", "No summary provided.")
    scam_type = data.get("scam_type", "General")
    top_flags = data.get("top_flags", [])

    response_message = generate_chatbot_response(risk_score, risk_level, summary, scam_type, top_flags)
    return jsonify({"response": response_message})

def generate_chatbot_response(risk_score, risk_level, summary, scam_type, top_flags):
    response = f"Hello! I\'m your financial risk assessment chatbot.\n\n"

    # Explain risk score
    response += f"Your risk score is {risk_score} out of 100. "
    if risk_score >= 80:
        response += "This indicates a very high potential risk."
    elif risk_score >= 60:
        response += "This indicates a high potential risk."
    elif risk_score >= 40:
        response += "This indicates a moderate potential risk."
    else:
        response += "This indicates a low potential risk."
    response += "\n\n"

    # Explain why the message is risky using flags
    if top_flags:
        response += "Here\'s why this message is flagged as risky: "
        for flag in top_flags:
            response += f"- {flag}. "
        response += "\n\n"
    elif summary != "No summary provided.":
        response += f"Summary of the message: {summary}.\n\n"

    # Recommended next steps based on risk level
    response += "Recommended next steps: "
    if risk_level == "High":
        response += "This is a high-risk situation. We strongly advise you NOT to send any money or share personal information. Please report this suspected scam immediately to your bank and relevant authorities."
    elif risk_level == "Medium":
        response += "This is a medium-risk situation. It\'s crucial to verify the sender\'s identity through an independent channel (not relying on contact details in the message). Pause any actions and do not click on any links until you are certain of its legitimacy."
    elif risk_level == "Low":
        response += "This appears to be a low-risk situation, but always stay cautious. Verify details independently if anything seems unusual. It\'s always better to be safe than sorry!"
    response += "\n\n"
    
    response += "Remember, I am a demo chatbot for a hackathon and do not provide real financial advice. Always consult with a qualified financial advisor for personalized guidance."

    return response

if __name__ == "__main__":
    app.run(debug=True, port=5000)
