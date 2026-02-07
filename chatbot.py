import requests

class PurdueChatbot:
    def __init__(self, api_key):
        self.api_url = "https://genai.rcac.purdue.edu/api/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.messages = []  # chat memory

    def ask(self, user_input):
        self.messages.append({
            "role": "user",
            "content": user_input
        })

        body = {
            "model": "llama3.1:latest",
            "messages": self.messages,
            "stream": False
        }

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=body
        )

        if response.status_code != 200:
            raise Exception(response.text)

        data = response.json()
        reply = data["choices"][0]["message"]["content"]

        self.messages.append({
            "role": "assistant",
            "content": reply
        })

        return reply
