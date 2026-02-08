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
      body: JSON.stringify({
        name,
        email,
        message
      })
    });

    if (response.ok) {
      navigate("/results");
    } else {
      setError("Failed to submit form.");
    }
  };

  return (
    <div>
      <h1>Intake Form</h1>

      <label>
        Name of sender (if applicable)
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>

      <br />

      <label>
        Email address of sender (if applicable)
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </label>

      <br />

      <label>
        Message *
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          required
        />
      </label>

      <br />

      {error && <p style={{ color: "red" }}>{error}</p>}

      <button onClick={handleSubmit}>Submit Form</button>
    </div>
  );
}

export default IntakeForm;
