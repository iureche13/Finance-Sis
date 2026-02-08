import React from "react";
import "./styles.css";

function ChatWindow({ messages }) {
  return (
    <div className="chat-window">
      {messages.map((msg, idx) => (
        <div
          key={idx}
          className={msg.role === "user" ? "message-user" : "message-assistant"}
        >
          {msg.content}
        </div>
      ))}
    </div>
  );
}

export default ChatWindow;
