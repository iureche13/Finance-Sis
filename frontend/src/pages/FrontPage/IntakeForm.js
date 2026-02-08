import { useState } from "react";
import { useNavigate } from "react-router-dom";

function IntakeForm() {
  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    if (message.trim() === "") {
      setError("Message is required.");
      return;
    }

    const response = await fetch("http://localhost:5001/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, message })
    });

    if (response.ok) {
      navigate("/results");
    } else {
      setError("Failed to submit form.");
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: "Arial, sans-serif"
      }}
    >
      {/* Title */}
      <h1 style={{ fontSize: "3rem", marginBottom: "2rem" }}>
        Scam Detector
      </h1>

      {/* Form Container */}
      <div
        style={{
          display: "flex",
          alignItems: "flex-start",
          gap: "3rem"
        }}
      >
        {/* FinanceSis label */}
        <h2 style={{ fontSize: "2rem", marginTop: "0.5rem" }}>
          FinanceSis
        </h2>

        {/* Form */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "1.5rem",
            width: "400px"
          }}
        >
          <label style={{ fontSize: "1.2rem" }}>
            Name of sender (if applicable)
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              style={{
                width: "100%",
                padding: "0.75rem",
                fontSize: "1.1rem",
                marginTop: "0.5rem"
              }}
            />
          </label>

          <label style={{ fontSize: "1.2rem" }}>
            Email address of sender (if applicable)
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              style={{
                width: "100%",
                padding: "0.75rem",
                fontSize: "1.1rem",
                marginTop: "0.5rem"
              }}
            />
          </label>

          <label style={{ fontSize: "1.2rem" }}>
            Message *
            <textarea
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              required
              style={{
                width: "100%",
                padding: "0.75rem",
                fontSize: "1.1rem",
                marginTop: "0.5rem",
                minHeight: "120px"
              }}
            />
          </label>

          {error && (
            <p style={{ color: "red", fontSize: "1.1rem" }}>{error}</p>
          )}

          <button
            onClick={handleSubmit}
            style={{
              padding: "0.75rem",
              fontSize: "1.2rem",
              cursor: "pointer",
              marginTop: "1rem"
            }}
          >
            Submit Form
          </button>
        </div>
      </div>
    </div>
  );
}

export default IntakeForm;