import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [inputMessage, setInputMessage] = useState('');
  const [chatMessages, setChatMessages] = useState([]);
  useEffect(() => {
    setChatMessages([{ role: 'bot', content: 'Welcome to the HR Chatbot! How can I help you?' }]);
  }, []);

  const handleSendMessage = async () => {
    if (inputMessage.trim()) {
      const newMessage = { role: 'user', content: inputMessage };
      setChatMessages([...chatMessages, newMessage]);
      setInputMessage('');

      // Placeholder for actual API request to your backend/ChatGPT
      const botResponse = await getBotResponse(inputMessage);
      setChatMessages((prev) => [...prev, { role: 'bot', content: botResponse }]);
    }
  };

  const getBotResponse = (userMessage) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve("This is a simulated response to: " + userMessage);
      }, 1000);
    });
  };

  return (
    <div className="app-container">
      <h1>HR Chatbot Frontend Simple Demo</h1>
      <div className="chat-container">
        <div className="chat-box">
          {chatMessages.map((message, index) => (
            <div key={index} className={message.role === 'user' ? 'user-message' : 'bot-message'}>
              {message.content}
            </div>
          ))}
        </div>
        <div className="input-container">
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            placeholder="Type a message..."
          />
          <button onClick={handleSendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
