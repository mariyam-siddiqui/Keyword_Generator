# 🔖 Keyword Tag Generator (with Ollama)

This is a web-based tool built using **Flask** and **Ollama** that allows you to generate meaningful **keyword tags** from any given text or document snippet.

Whether you need to **auto-tag emails**, **organize documents**, or **improve searchability**, this tool uses an open-source LLM to suggest relevant keywords in real-time — with a sleek, futuristic dark UI and a copy-to-clipboard feature.

---

## 🌟 Why I Built This

While managing emails and document summaries, I often needed a quick way to **tag content** with relevant keywords. Manual tagging was inefficient, inconsistent, and time-consuming.

So I built this app as a personal tool to:
- Quickly extract **semantic keywords**
- Use **open-source models locally** (instead of paid APIs)
- Learn more about **LLMs and local inference**

---

## 🧠 How It Works

The app uses [**Ollama**](https://ollama.com/) to run a language model locally (e.g. `llama3`) and generate tags for any user-provided input.

- **Frontend**: A minimal HTML + JavaScript app served by Flask
- **Backend**: Flask server sends the input to Ollama for inference
- **Model**: `llama3.2` queried via a system/user prompt chat completion
- **Output**: Comma-separated tags based on the input

---

## 🧪 What is Ollama?

[**Ollama**](https://ollama.com) is a fast and easy-to-use tool that allows you to run LLMs (like LLaMA, Mistral, Phi, etc.) **locally** on your machine with a single command.

### 🔧 How Ollama Works Under the Hood:

1. Ollama runs a **local REST API** at `http://localhost:11434`
2. You install and load models like `llama3`, `mistral`, `phi` locally
3. You call the models using a standard OpenAI-compatible interface
4. Your data never leaves your machine — **privacy-friendly and offline**

### 🚀 To Get Started with Ollama:

1. Download & install Ollama:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh


🤖 Using Hugging Face Instead
If you don't want to run models locally, you can replace Ollama with Hugging Face Inference API using a model like facebook/bart-large-mnli for zero-shot keyword classification. This requires no GPU but does need a Hugging Face account and token.

Want that version? Check the Hugging Face branch [→ coming soon]


🛠️ How to Run This Project Locally
1. Clone the repo
git clone https://github.com/mariyam-siddiqui/Keyword_Generator.git
cd Keyword_Generator

2. Set up a Python virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies
pip install -r requirements.txt

4. Start Ollama and load the model
ollama run llama3.2

5. Run the Flask app
python app.py


Open your browser and go to http://127.0.0.1:5000


✨ Features
Beautiful dark UI with glowing neon effects

Copy tags button to easily paste into other tools

Runs completely locally using open-source models

No API cost, no data sharing, no cloud dependency

🧩 Future Improvements
Add support for Hugging Face API (fallback mode)

Store past tagged documents

Build a REST API for batch tagging

Package as a desktop app
