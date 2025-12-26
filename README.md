## 🤖 CareerBot — AI Career Assistant Agent

---

<p align="center">
  <strong>An AI-powered personal career assistant that represents you professionally on your website</strong><br/>
  Built with Gemini, Gradio & UV ⚡
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/UV-Package%20Manager-purple" />
  <img src="https://img.shields.io/badge/AI-Gemini-orange" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

---
## 🔗🌐 Working Link:
- Will Upload soon...

## 🌟 Why CareerBot?

CareerBot is a **production-style AI agent** that acts as a **digital version of you** — answering questions about your **career, skills, experience, and projects** using your **resume, LinkedIn profile, and personal summary**.

Perfect for:
- 💼 Personal portfolio websites  
- 🤝 Recruiter-facing AI assistants  
- 🧠 AI agent architecture demos  
- 🚀 Resume & GitHub profile enhancement  

---

## ✨ Features

- 🤖 **AI Career Representation**  
  Responds like a real professional — not a generic chatbot.

- 📄 **PDF Knowledge Extraction**  
  Reads and understands:
  - Resume (PDF)
  - LinkedIn profile (PDF)

- 🧠 **Context-Persistent System Prompting**  
  Ensures answers stay accurate, professional, and in-character.

- 🛠 **AI Tool Calling (Function Calling)**  
  - Captures visitor name & email  
  - Logs unknown or unanswerable questions  

- 🔔 **Real-Time Notifications**  
  Push alerts via **Pushover API** whenever:
  - A visitor shares contact info  
  - The bot encounters an unknown question  

- 💬 **Web Chat Interface**  
  Clean UI using **Gradio ChatInterface**

- ⚡ **UV Package Manager**  
  Ultra-fast installs, reproducible builds, modern Python workflow.

---

## 🧠 How It Works

Loads career documents (Resume, LinkedIn, Summary)

Builds a strong system prompt

Uses Gemini for reasoning & responses

Invokes tools automatically when needed

Sends real-time notifications

Serves an interactive web chat UI

This is a true AI agent pattern, not just a chatbot.

---

## 🛠 AI Tools Used

- 📌 recordUserDetails

Captures visitor contact details and notifies the owner.

- ❓ recordUnknownQuestion

Logs unanswered questions for improvement and follow-up.

- 🔐 Security & Privacy

- 🔒 Secrets managed via .env

- 🚫 No database used (stateless & secure)

- 🧹 .env and .venv excluded from version control

- 🌱 Roadmap

- 📊 Conversation analytics dashboard

- 📧 Email notifications & CRM sync

- 🧠 Vector embeddings (RAG)

- 🐳 Docker support

- ☁️ Cloud deployment (Vercel / Fly.io / AWS)

---

## 🗂 Project Structure

```text
CAREERBOT/
│
├── .git/                  # Git repository
├── .venv/                 # UV-managed virtual environment
├── Profile/
│   ├── Profile.pdf        # LinkedIn profile
│   ├── Resume.pdf         # Resume
│   └── me.txt             # Personal summary
│
├── .env                   # Environment variables
├── .gitignore
├── .python-version
├── main.py                # Application entry point
├── pyproject.toml         # UV project config
├── uv.lock                # Dependency lock file
└── README.md

```

## 🚀 Installation & Usage

1️⃣ Clone the Repo:

    git clone https://github.com/Pratyush112/Career-Bot-Agent
Change the directory to careerbot using the command in terminal: 
    
    cd careerbot

2️⃣ Install Dependencies (UV) use this command in the terminal: 

    `uv sync`

3️⃣ Configure Environment Variables:

    Create a .env file and store your api keys

4️⃣ Run the Bot:

Open the terminal and run this command

    uv run python main.py
    Open the local Gradio URL in your browser 🎉


---

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`GEMINI_API_KEY` = your_gemini_api_key

`PUSHOVER_USER_KEY` = your_pushover_user_key

`PUSHOVER_API_TOKEN` = your_pushover_app_token


This project demonstrates:

AI agent architecture, Real-world tool calling, Clean prompt engineering, Production-ready Python practices.

---

## 🧰 Tech Stack
| Parameter       | Type                     | 
| :-------------- | ------------------------ |
| Layer           | Technology	             |
|Language	      | Python 3.10+             |
|AI Model	      | Gemini (gemini-2.5-flash)|
|UI	              | Gradio                   |
|PDF Parsing	  | pypdf                    |
|Env Management	  | python-dotenv            |
|HTTP	          | requests                 |
|Package Manager  | UV                       |
|Notifications	  | Pushover API             |


---

## If you find this useful:
- ⭐ Support the Project

- ⭐ Star the repository

- 🍴 Fork it

- 💡 Suggest improvements

- 📢 Share with others

---

```
## Authors

- [@Pratyush](https://www.github.com/Pratyush112)

---