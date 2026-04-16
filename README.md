# chat-bot
# 💬 Real-Time Chat Application

## 📌 Overview

This project is a real-time chat application built using FastAPI and WebSockets. It allows multiple users to communicate instantly in chat rooms, with support for message handling, file uploads, and persistent storage using SQLite.

The application demonstrates modern backend development concepts including asynchronous communication, API design, and real-time data exchange.

---

## 🚀 Features

* ⚡ Real-time messaging using WebSockets
* 👥 Multi-user chat room support
* 💾 Persistent message storage with SQLite
* 📂 File upload functionality
* 🌐 Dynamic frontend using HTML, CSS
* 🔄 Fast and asynchronous backend with FastAPI

---

## 🛠 Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Communication:** WebSockets

---

## 📁 Project Structure

```
chat-app/
├── main.py           # FastAPI backend with WebSocket handling
├── requirements.txt # Project dependencies
├── chat.db          # SQLite database (auto-generated)
├── uploads/         # Stores uploaded files
├── static/
│   ├── style.css    # Styling
│   └── app.js       # JavaScript (currently unused)
├── templates/
│   ├── index.html   # Homepage
│   └── chat.html    # Chat interface
└── models/
    └── room.py      # Database operations
```

---

## ⚙️ How It Works

* Users join a chat room through the web interface
* A WebSocket connection is established with the FastAPI server
* Messages are sent and received in real-time
* Data is stored in SQLite for persistence
* Uploaded files are saved in the `uploads/` directory

---

## ▶️ How to Run

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Run the server:

   ```
   uvicorn main:app --reload
   ```

3. Open in browser:

   ```
   http://127.0.0.1:8000
   ```

---

## 📈 Future Improvements

* 🔐 User authentication (login/signup)
* 📱 Responsive UI design
* 🧠 AI chatbot integration
* ☁️ Deployment on cloud (Render / AWS)
* 🔔 Notifications system

---

## 📌 Conclusion

This project is a strong demonstration of real-time web application development using FastAPI and WebSockets. It showcases backend efficiency, asynchronous programming, and practical full-stack integration.

---

