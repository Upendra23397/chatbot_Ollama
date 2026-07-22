````markdown
# 🤖 AI Chatbot with LangChain & Ollama

A simple AI chatbot built using **Python**, **LangChain**, and **Ollama**. The chatbot supports different personalities (Angry, Funny, and Sad) and runs **locally** without requiring any cloud API.

## 🚀 Features

- 💬 Interactive chatbot
- 😡 Angry mode
- 😂 Funny mode
- 😢 Sad mode
- 🧠 Conversation memory
- 🖥️ Runs completely on your local machine using Ollama
- 🔒 No API key required

---

## 📂 Project Structure

```
project/
│── app.py
│── requirements.txt
│── README.md
└── .venv/
```

---

## 🛠️ Prerequisites

- Python 3.10+
- Ollama installed

Download Ollama:

https://ollama.com/download

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama Model

Download the Llama model:

```bash
ollama pull llama3.2
```

Verify installation:

```bash
ollama list
```

---

## ▶️ Run the Application

```bash
python app.py
```

If you're using Streamlit:

```bash
streamlit run app.py
```

---

## 🎭 Available Modes

| Option | Description |
|--------|-------------|
| 1 | Angry AI |
| 2 | Funny AI |
| 3 | Sad AI |

---

## 📚 Technologies Used

- Python
- LangChain
- Ollama
- Streamlit (optional)

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
langchain
langchain-core
langchain-ollama
streamlit
```

---

## ⚠️ Notes

- Ollama must be installed before running the project.
- The required model (e.g. `llama3.2`) must be downloaded using:

```bash
ollama pull llama3.2
```

- This project runs locally and does not require an API key.

---

## 📄 License

This project is provided for educational purposes. Feel free to modify and extend it.
````
