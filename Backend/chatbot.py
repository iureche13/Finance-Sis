import requests
import json

class RiskAssessmentChatbot:
    def __init__(self, api_key, risk_data_path):
        self.api_key = api_key

        with open(risk_data_path, "r") as f:
            self.risk_data = json.load(f)

        self.endpoint = "https://genai.rcac.purdue.edu/api/chat/completions"

    def ask(self, user_message):
        system_prompt = self._build_system_prompt()

        body = {
            "model": "llama3.1:latest",
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "stream": False,
            "temperature": 0.4
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            self.endpoint,
            headers=headers,
            json=body,
            timeout=30
        )

        if response.status_code != 200:
            raise Exception(f"Llama API error: {response.status_code}, {response.text}")

        data = response.json()
        return data["choices"][0]["message"]["content"]

    def _build_system_prompt(self):
        return f"""
You are a financial risk assessment chatbot.

You have access to a user's scam risk assessment data and must answer questions
based on that data as well as general scam and fraud detection knowledge.

USER RISK DATA:
- Risk Score: {self.risk_data["risk_score"]} / 100
- Risk Level: {self.risk_data["risk_level"]}

CONCERNING AREA:
- Concerning area of message: {self.risk_data["concerning_area"]}

SUMMARY:
{self.risk_data["summary"]}

TOP WARNING FLAGS:
{", ".join(self.risk_data["flags"])}

CONCERNS ABOUT EMAIL ADDRESS:
{", ".join(self.risk_data["email_concerns"])}

The USER RISK DATA and SUMMARY fields will always be populated but the 
CONCERNING AREA, TOP WARNING FLAGS, and CONCERNS ABOUT EMAIL ADDRESS fields 
may be empty. If a field is empty, do not include anything about that field 
in your answer. If the user inquires about these fields and they are missing/empty,
indicate that you do not have any information about those fields from the message
they provided.

INSTRUCTIONS:
- Explain the risk score and level when asked
- Answer follow-up questions conversationally
- Provide general scam prevention advice
- Do NOT provide legal or financial advice
- Be clear, calm, and supportive
"""
