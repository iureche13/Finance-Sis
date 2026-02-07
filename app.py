from flask import Flask, request, jsonify, render_template
from chatbot import PurdueChatbot  # if you split files

app = Flask(__name__)

chatbot = PurdueChatbot(api_key="")

# Mock UI route
@app.route("/")
def index():
    return render_template("index.html")  # This is your HTML chat UI

@app.route("/chat", methods=["POST"])
def chat():
    try: 
        user_msg = request.json["message"]
        print(f"Received message: {user_msg}")
        reply = chatbot.ask(user_msg)
        return jsonify({"reply": reply})
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"reply": "Internal Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
