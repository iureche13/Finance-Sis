# Finance-Sis Scam Detector

This is a chatbot web application for a hackathon tailored towards young women, especially college students (such as at Purdue!). It assesses financial risk based on provided inputs and offers tailored advice to detect whether the financial offer is a scam by giving a risk score, summary and chatbot to ask follow-up questions. We want to encourage financial safety for women especially because they have historically lower financial literacy awareness than men.

## Features

*   **Risk Assessment:** Explains risk scores, identifies risky flags, and provides recommended next steps.
*   **UI:** Chat interface for interaction with chatbot advisor, including a summary and risk score (color coded)

## Setup and Running Locally

Follow these steps to get the chatbot running on your local machine.

### Prerequisites

The simplest way to run our project is to make a virtual environment to easily install all required dependencies.

### 1. Run Final.py for the Intake Form

Open your terminal or command prompt in the project directory and run python Final.py.

```bash
python Final.py
```


### 2. Run the Backend

In another terminal, run the Flask application to connect to the chatbot (Your own API key must be provided in app.py):

```bash
python app.py
```

This will start the Flask development server.

### 3. Access the UI

In another terminal, go to the Frontend folder. Run 'npm install' and then run 'npm start' (make sure node and npm are installed).

```bash
npm start
```

### 4. Using the Application
Fill out the form (email and sender are optional), submit it, and get access to your personalized risk score page! Feel free to ask the chatbot follow-up questions or general questions about financial scams. Please take a look at the risk score and the summary.


## Important Notes

*   This chatbot is a **demo for a hackathon** and does not provide real financial advice. Always consult with a qualified financial advisor for personalized guidance.
