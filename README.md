🗄️ PyKV – A Scalable In-Memory Key-Value Store with Persistence

PyKV is a lightweight, scalable in-memory key-value store implemented in Python using FastAPI.
It combines high-performance LRU caching, disk-based persistence, crash recovery, and RESTful APIs, along with a CLI client and a web-based UI.

This project is designed for academic evaluation, systems learning, and backend architecture demonstrations.

📌 Key Features

🚀 Fast In-Memory Storage

Uses an LRU (Least Recently Used) cache for O(1) read/write operations

Configurable cache capacity (default: 5 keys)

💾 Persistence (Durability)

Implements Write-Ahead Logging (WAL)

Every operation is appended to a disk log (data.log)

🔁 Crash Recovery

On server restart, the system replays the log file

Restores the last consistent in-memory state automatically

🔗 REST API (FastAPI)

SET, GET, DELETE, and LIST KEYS operations

JSON-based request/response model

🧪 CLI Client

Interactive terminal client

Supports benchmarking and functional testing

🌐 Web UI

Simple HTML + JavaScript frontend

Real-time interaction with backend APIs

🔄 Replication Hook

Placeholder for future multi-node replication

🏗️ Project Architecture
UI / CLI Client
      ↓
FastAPI Server (main.py)
      ↓
KeyValueStore (store.py)
      ↓
LRU Cache (lru_cache.py)
      ↓
Persistence Log (persistence.py → data.log)

📂 Project Structure
PYKV PYTHON/
│
├── ui/
│   ├── index.html        # Web UI
│   ├── script.js         # UI → API communication
│   └── style.css         # UI styling
│
├── client.py             # CLI client
├── main.py               # FastAPI server
├── store.py              # Core key-value logic
├── lru_cache.py          # LRU cache implementation
├── persistence.py        # Disk logging & recovery
├── replication.py        # Replication hook
├── models.py             # Request models
├── data.log              # Persistent operation log
├── requirements.txt      # Dependencies
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/PyKV-Python.git
cd PyKV-Python

2️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Project
🔹 Start the Backend Server
python -m uvicorn main:app --reload


Server runs at:

http://127.0.0.1:8000


FastAPI Docs:

http://127.0.0.1:8000/docs

🔹 Run the CLI Client
python client.py


Supported operations:

SET key

GET key

DELETE key

LIST ALL KEYS

BENCHMARK

🔹 Run the Web UI
Option 1: Open directly

Open:

ui/index.html


in your browser.

Option 2: Using Live Server (VS Code)

Right-click index.html

Click Open with Live Server

🔌 API Endpoints
Method	Endpoint	Description
POST	/set	Store key-value pair
GET	/get/{key}	Retrieve value
DELETE	/{key}	Delete key
GET	/keys	List all keys
🔁 Crash Recovery Example

Insert key-value pairs

Stop the server

Restart the server

Stored keys are automatically restored from data.log

🧪 Benchmarking

The CLI client includes a benchmark option:

Inserts multiple key-value pairs

Measures total execution time

Demonstrates performance impact of logging and cache eviction

📚 Technologies Used

Python 3

FastAPI

Uvicorn

AsyncIO

HTML / CSS / JavaScript

LRU Cache (OrderedDict)

🎓 Academic Relevance

This project demonstrates:

In-memory data structures

Cache eviction policies

Write-ahead logging

Crash recovery mechanisms

REST API design

Client-server architecture

Suitable for:

System Design

Distributed Systems (intro)

Backend Engineering

Mini / Capstone Projects

🚀 Future Enhancements

Multi-node replication

Snapshot-based persistence

Authentication & authorization

Configurable eviction policies

Distributed deployment
