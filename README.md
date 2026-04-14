# 🤖 Role-Based LLM Chatbot

A professional Python application that demonstrates **LLM Orchestration** and **System Prompting**. This chatbot allows users to interact with an AI model under different personas, showcasing how "System Messages" influence AI behavior and tone.

---

## 🚀 Features
* **Role Selection:** Choose between a Python Tutor, Fitness Coach, or Travel Guide.
* **Persistent Memory:** Full chat history management ensures the AI remembers context within a session.
* **Web Interface:** Built with **Streamlit** for a modern, user-friendly experience.
* **Local LLM:** Powered by **Ollama** (Llama 3.2), ensuring data privacy and no API costs.

---

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Frontend:** Streamlit
* **LLM Engine:** Ollama (Model: `llama3.2:3b`)
* **Version Control:** Git & GitHub

---

## 📦 Installation & Setup

### 1. Prerequisites
Ensure you have [Ollama](https://ollama.com/) installed and the model downloaded:
```bash
ollama pull llama3.2:3b