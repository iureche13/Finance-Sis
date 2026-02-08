import React, { useState, useEffect } from "react";
import ChatWindow from "./ChatWindow";
import MessageInput from "./MessageInput";
import RiskCircle from "./RiskCircle";

function ResultsPage() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hi! I’m your risk assessment assistant." }
  ]);

  const [riskScore, setRiskScore] = useState(null);
  const [riskLevel, setRiskLevel] = useState(null);
  const [summary, setSummary] = useState(""); // <- Step 1: add state

  // Step 2: fetch risk data including summary
  useEffect(() => {
    fetch("http://localhost:5000/risk")
      .then(res => res.json())
      .then(data => {
        setRiskScore(data.risk_score);
        setRiskLevel(data.risk_level);
        setSummary(data.summary || ""); // <- Step 3: set summary
      })
      .catch(err => console.error(err));
  }, []);

  const handleSend = async (text) => {
    setMessages(prev => [...prev, { role: "user", content: text }]);

    try {
      const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
      });

      const data = await response.json();
      setMessages(prev => [...prev, { role: "assistant", content: data.reply }]);
      
      if (data.risk_score) setRiskScore(data.risk_score);
      if (data.risk_level) setRiskLevel(data.risk_level);
      if (data.summary) setSummary(data.summary); // <- update summary if returned

    } catch (err) {
      setMessages(prev => [...prev, { role: "assistant", content: "Error contacting server." }]);
      console.error(err);
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "20px auto" }}>
      <h1>Your Personalized Risk Assessment</h1>

      {riskScore !== null && (
  <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
    {/* Risk Circle on the left */}
    <RiskCircle score={riskScore} />

    {/* Summary on the right */}
    {summary && (
      <div
        style={{
          marginLeft: "20px",
          backgroundColor: "#ffe6f0",
          padding: "10px 15px",
          borderRadius: "8px",
          boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
          maxWidth: "350px",
          fontSize: "14px",
          color: "#555",
        }}
      >
        <strong>Summary:</strong>
        <p style={{ margin: "5px 0 0 0" }}>{summary}</p>
      </div>
    )}
  </div>
)}


      <ChatWindow messages={messages} />
      <MessageInput onSend={handleSend} />
    </div>
  );
}

export default ResultsPage;
