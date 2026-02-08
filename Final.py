import json
from NLPProcessing import calculate_score, keyword_score
from CheckIdentity import calculate_risk_score, name_in_email
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    name = data.get("name", "")
    email = data.get("email", "")
    message = data.get("message", "")

    if not message.strip():
        return jsonify({"error": "Message required"}), 400

    # File in same directory as Final.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "submissions.txt")

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(name + "\n")
        f.write(email + "\n")
        f.write(message + "\n")
        f.write("-----\n")

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(port=5000, debug=True)


def save_results_to_json(risk_score, risk_level, flags, concerning_area, email_concerns, summary, filename):
    data = {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "flags" : flags,
        "concerning_area" : concerning_area,
        "email_concerns" : email_concerns,
        "summary" : summary
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Data saved to {filename}")

def generate_summary(risk_score, risk_level, flags, email_concerns):
    summary = f"This message has a risk score of {risk_score}, which is considered to be {risk_level.lower()}."
    phrases = ""
    if len(flags) > 0:
        for i in range(len(flags)):
            phrases += f"\"{flags[i]}\""
            if i == len(flags) - 2:
                phrases += " and "
            elif i == len(flags) - 1:
                phrases += ''
            else:
                phrases += ", "
    if len(phrases) > 0:
        summary += f" Some concerning phrases, including {phrases} raise cause for suspicion."
    emails = ""
    if len(email_concerns) > 0:
        for i in range(len(email_concerns)):
            emails += f"{email_concerns[i]}"
            if i == len(email_concerns) - 2:
                emails += " and "
            elif i == len(email_concerns) - 1:
                emails += ''
            else:
                emails += ", "
    if len(emails) > 1:
        summary += f" There are concerning aspects of the email address, including {emails}"
    elif len(emails) > 0:
        summary += f"There is a concerning aspect of the email address: {emails}"
    return summary

def final_score_and_status(email_score, message_score):
    if email_score > -1:
        score = email_score * .3 + message_score * .7
    else:
        score = message_score
    # Categorize Risk
    if score > 60:
        status = "high"
    elif score > 30:
        status = "moderate"
    else:
        status = "low"
    return int(score), status

def get_scam_words(file):
    fileptr = open(file)
    search_words = {}
    current_category = ""
    for line in fileptr:
        line = line.lower()
        line = line.strip("\n")
        line = line.rstrip()
        if "category" in line:
            category = line.split(":")[1].strip()
            search_words[category] = []
            current_category = category
        else:
            search_words[current_category].append(line)
    fileptr.close()
    return search_words

file = 'scam_words'
search_words = get_scam_words(file)
filename = 'Backend/data.json'

def run_program(name, email, message):
    message_score, concerning_area, flags = keyword_score(search_words, message)
    email_score, email_concerns = calculate_risk_score(name, email)
    risk_score, risk_level = final_score_and_status(email_score, message_score)
    summary = generate_summary(risk_score, risk_level,flags, email_concerns)
    save_results_to_json(risk_score, risk_level, flags, concerning_area, email_concerns, summary, filename)
    return summary

name = "Colette Bacidore"
email = "colettegba@gmail.com"
message = "too good to be true, this is a great deal. there is a Special discount, Warranty, and great wealth."
print(run_program(name, email, message))
