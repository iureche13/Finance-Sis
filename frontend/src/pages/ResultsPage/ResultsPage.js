import React, { useState, useEffect } from "react";
import ChatWindow from "./ChatWindow";
import MessageInput from "./MessageInput";

function ResultsPage() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hi! I’m your risk assessment assistant." }
  ]);

  const [riskScore, setRiskScore] = useState(null);
  const [riskLevel, setRiskLevel] = useState(null);

  // Optional: fetch initial risk data from backend on load
  useEffect(() => {
    fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: "Show my risk score" })
    })
      .then((res) => res.json())
      .then((data) => {
        // If backend includes risk_score & risk_level in response
        if (data.risk_score) setRiskScore(data.risk_score);
        if (data.risk_level) setRiskLevel(data.risk_level);
      })
      .catch((err) => console.error(err));
  }, []);

  const handleSend = async (text) => {
    // Add user message
    setMessages((prev) => [...prev, { role: "user", content: text }]);

    try {
      const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
      });

      const data = await response.json();
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: data.reply }
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Error contacting server." }
      ]);
      console.error(err);
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "20px auto" }}>
      <h1>Risk Assessment Chatbot</h1>
      {riskScore !== null && riskLevel && (
        <div className="risk-box">
          <strong>Risk Score:</strong> {riskScore} / 100 | <strong>Level:</strong>{" "}
          {riskLevel}
        </div>
      )}
      <ChatWindow messages={messages} />
      <MessageInput onSend={handleSend} />
    </div>
  );
}

export default ResultsPage;
