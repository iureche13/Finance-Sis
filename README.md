# Financial Risk Chatbot Demo

This is a simple Flask-based chatbot web application for a hackathon demo. It assesses financial risk based on provided inputs and offers tailored advice.

## Features

*   **Risk Assessment:** Explains risk scores, identifies risky flags, and provides recommended next steps.
*   **Simple UI:** Basic chat interface for interaction.
*   **Mock Data:** Includes a button to quickly populate with sample risk data for demonstration.

## Setup and Running Locally

Follow these steps to get the chatbot running on your local machine.

### Prerequisites

Make sure you have Python 3 and `pip` installed.

### 1. Install Dependencies

Open your terminal or command prompt in the project directory (`c:/Users/nandi/Downloads/Finance-Sis`) and install the required Python packages:

```bash
pip install Flask
```

### 2. Run the Backend

In the same terminal, run the Flask application:

```bash
python app.py
```

This will start the Flask development server, typically on `http://127.0.0.1:5000/` or `http://localhost:5000/`.

### 3. Access the Chatbot

Open your web browser and navigate to `http://localhost:5000/`.

You can then:

*   **Enter Custom Data:** Input your own JSON data into the text field, following this structure:

    ```json
    {
        "risk_score": 75,
        "risk_level": "Medium",
        "summary": "An email asking for urgent wire transfer to an unknown account.",
        "scam_type": "Phishing",
        "top_flags": ["Urgent request", "Unknown sender", "Request for money"]
    }
    ```

*   **Use Mock Data:** Click the "Mock Data" button to send a pre-filled example of high-risk data.

## Project Structure

*   `app.py`: The Flask backend application, handling routing and chatbot logic.
*   `templates/index.html`: The frontend HTML, CSS, and JavaScript for the chat interface.
*   `README.md`: This file, providing setup and usage instructions.

## Important Notes

*   This chatbot is a **demo for a hackathon** and does not provide real financial advice. Always consult with a qualified financial advisor for personalized guidance.
*   The chatbot **does NOT calculate the risk score**; it only processes the `risk_score`, `risk_level`, `summary`, `scam_type`, and `top_flags` that you provide.
