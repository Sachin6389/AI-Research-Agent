# 🤖 AI Research Agent

## 📌 Project Title

**AI Research Agent – Autonomous Web Research & Report Generation using LangGraph**

---

## 📖 Project Description

The **AI Research Agent** is an AI-powered research assistant built using **React.js, Python, LangGraph, LangChain, Groq LLM, and Tavily Search API**.

The application allows users to enter a research topic or question, searches the web for relevant information, reads and analyzes webpages, summarizes the collected information, and generates a structured research report.

Unlike a traditional chatbot that relies only on the knowledge stored inside an LLM, this AI Research Agent dynamically searches the web and uses the retrieved information as context before generating its final response.

The agent workflow is orchestrated using **LangGraph**, allowing multiple steps such as web searching, webpage reading, summarization, and report generation to work together as an intelligent workflow.

The project demonstrates how **Agentic AI + LLMs + Web Search + LangGraph** can be combined to build an autonomous research system.

---

## ✨ Features

* 🤖 AI-powered autonomous research agent
* 🔍 Real-time web search using Tavily API
* 🌐 Webpage content extraction and reading
* 🧠 LLM-powered content summarization
* 📝 Automatic research report generation
* 🔗 Source-based research workflow
* 🕸️ Multi-step agent workflow using LangGraph
* ⚡ Fast responses using Groq LLM
* 🧩 LangChain integration
* 📚 Research from multiple web sources
* 🎯 Context-aware research results
* 📄 Structured research reports
* 💬 Interactive React chat/research interface
* 🔄 State-based workflow management
* 🔐 Secure API key management using environment variables
* 🔗 React frontend and Python backend integration
* 🚀 Easily extendable for advanced AI agent workflows

---

# 🛠 Technologies Used

## Frontend

* React.js
* Vite
* JavaScript
* CSS
* Axios
* React Components
* React Markdown
* Remark GFM

## Backend

* Python
* Flask
* Flask-CORS
* LangChain
* LangGraph
* LangChain Groq
* Tavily Search API
* Python Dotenv
* Gunicorn

## AI & Agentic AI Stack

* Generative AI
* Large Language Models (LLMs)
* Agentic AI
* LangGraph
* LangChain
* Groq LLM
* Tavily Web Search
* Web Research
* Webpage Content Extraction
* Text Summarization
* Context-Aware Report Generation

## Development Tools

* Git
* GitHub
* VS Code
* Python Virtual Environment
* npm
* REST APIs

---

# 🏗️ AI Research Agent Architecture

The research process follows a multi-step workflow:

```text
                 User Research Question
                          │
                          ▼
                  React Frontend
                          │
                          ▼
                   Python Backend
                          │
                          ▼
                    LangGraph
                          │
                          ▼
                  Research Planning
                          │
                          ▼
                  Tavily Web Search
                          │
                          ▼
                Relevant Web Sources
                          │
                          ▼
                  Read Webpages
                          │
                          ▼
                   Summarize Content
                          │
                          ▼
                Generate Research Report
                          │
                          ▼
                  Final AI Response
                          │
                          ▼
                   React Frontend
```

---

# 📥 Installation Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Sachin6389/AI-Research-Agent.git

cd AI-Research-Agent
```

---

# ⚙️ Backend Setup

Navigate to the backend directory:

```bash
cd Backend
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

Activate:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Configure Environment Variables

Create a `.env` file inside the `Backend` directory.

```env
GROQ_API_KEY=
TAVILY_API_KEY=
```
---

# 🚀 Run Backend

From the `Backend` directory:

```bash
python app.py
```

The backend server will run on:

```text
http://localhost:5000
```

---

# ⚙️ Frontend Setup

Open another terminal and navigate to the project root:

```bash
cd AI-Research-Agent
```

Then navigate to the frontend:

```bash
cd Frontend
```

---

## Install Packages

```bash
npm install
```

---

## 🔐 Configure Frontend Environment Variables

Create:

```text
Frontend/.env
```

Add:

```env
VITE_BACKEND_URL=
```

---

## Start Development Server

```bash
npm run dev
```

The frontend will run on:

```text
http://localhost:5173
```

---

# 🚀 How the AI Research Agent Works

The agent follows a multi-step research workflow.

### Step 1 — User Input

The user enters a research question or topic.

Example:

```text
What are the latest developments in Generative AI?
```

### Step 2 — Research Planning

The LangGraph workflow receives the user's question and manages the research process.

### Step 3 — Web Search

The agent uses the **Tavily Search API** to find relevant webpages and information.

### Step 4 — Read Webpages

The agent retrieves useful information from the discovered webpages.

### Step 5 — Summarization

The collected information is summarized using the Groq LLM.

### Step 6 — Report Generation

The agent combines the relevant information and generates a structured research report.

### Step 7 — Final Response

The generated research report is returned to the React frontend and displayed to the user.

---

# 🧠 LangGraph Workflow

The project uses **LangGraph** to build and manage the research workflow.

A simplified workflow looks like:

```text
START
  │
  ▼
Research Question
  │
  ▼
Web Search
  │
  ▼
Read Webpages
  │
  ▼
Summarize Sources
  │
  ▼
Generate Report
  │
  ▼
END
```

LangGraph makes it possible to represent the research process as a collection of connected nodes and states.

Each node performs a specific task and passes information to the next stage of the workflow.

---

# 🔄 Research Pipeline

```text
User Query
    ↓
LangGraph State
    ↓
Tavily Search
    ↓
Search Results
    ↓
Webpage Reader
    ↓
Relevant Content
    ↓
Groq LLM
    ↓
Content Summaries
    ↓
Research Report
    ↓
React UI
```

---

# 📂 Project Structure

```text
AI-Research-Agent/
│
├── Backend/
│   │
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   ├── .gitignore
│   │
│   └── src/
│       ├── __init__.py
│       ├── State.py
│       ├── Tools.py
│       ├── Prompt.py
│       └── Graph.py
│
├── Frontend/
│   │
│   ├── src/
│   │   ├── assets/
│   │   ├── Components/
│   │   │   ├── Chatboat.jsx
│   │   │   ├── ChatInput.jsx
│   │   │   └── Message.jsx
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── public/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   ├── vercel.json
│   └── .gitignore
│
├── README.md
└── LICENSE
```
---

# 🔗 API Integration

The frontend communicates with the Python backend through REST APIs.

### Research Request

```http
POST /chat
```

Example request:

```json
{
  "query": " Large Language Models?"
}
```

Example response:

```json
{
  "response": "# Research Report: llm\n\n## 1. Executive Summary\n\nThe research question \"llm\" is answered by defining what LLM stands for and its meaning in the context of Artificial Intelligence (AI). LLM stands for Large Language Model, which is a type of language model trained on massive amounts of text to predict and generate natural language. The key features of LLMs include being large, focusing on linguistics, and utilizing the Transformer architecture.\n\n## 2. Introduction\n\nThe term \"llm\" has multiple meanings, but in the context of AI, it refers to Large Language Model. Understanding what LLM stands for and its applications is crucial in the field of natural language processing (NLP). LLMs have become a foundational technology behind modern chatbots and are used for various tasks such as generating, summarizing, translating, and analyzing text.\n\n## 3. Latest Findings\n\nThe latest information on LLMs indicates that they are typically based on transformer architecture, with generative pre-trained transformers (GPTs) being a type of LLM. Notable LLMs include BERT, GPT-1, GPT-2, GPT-3, and GPT-4. Additionally, open-weight LLMs and multimodal LLMs have been developed, allowing for more permissive usage and deployment.\n\n## 4. Key Developments\n\nThe development of LLMs has been rapid, with the first transformer-based models emerging in 2017. Since then, there have been significant advancements in the field, including the introduction of GPTs and the development of open-weight and multimodal LLMs. Tokenization is a crucial step in preparing text data for LLMs, with algorithms like byte-pair encoding (BPE) and WordPiece being used to convert text to numerical tokens.\n\n## 5. Evidence and Analysis\n\nThe evidence from the sources indicates that LLMs are a type of language model that utilizes the Transformer architecture to predict and generate natural language. The analysis of the sources suggests that LLMs have become a crucial technology in the field of NLP, with applications in chatbots, text generation, and language translation.\n\n## 6. Challenges and Limitations\n\nOne of the limitations of the research is that the term \"llm\" has multiple meanings, and it is essential to clarify the context in which it is being used. Additionally, the development of LLMs is a rapidly evolving field, and it is crucial to stay up-to-date with the latest advancements and developments.\n\n## 7. Conclusion\n\nIn conclusion, the research question \"llm\" is answered by defining what LLM stands for and its meaning in the context of AI. LLM stands for Large Language Model, which is a type of language model trained on massive amounts of text to predict and generate natural language.\n\n## 8. Sources\n\n* https://en.wikipedia.org/wiki/Large_language_model\n* https://llm-guide.com/what-is-an-llm\n* https://keymakr.com/blog/llm-meaning-what-does-the-abbreviation-llm-stand-for-in-ai-a-comprehensive-explanation\n\nNote: The source https://www.cloudflare.com/learning/ai/what-is-large-language-model was not directly relevant to the research question and required JavaScript and cookies to be enabled to access the content."
}
```

---

# 💬 Example Usage

### User Query

```text
llm?
```

### AI Research Agent

```text
"# Research Report: llm\n\n## 1. Executive Summary\n\nThe research question \"llm\" is answered by defining what LLM stands for and its meaning in the context of Artificial Intelligence (AI). LLM stands for Large Language Model, which is a type of language model trained on massive amounts of text to predict and generate natural language. The key features of LLMs include being large, focusing on linguistics, and utilizing the Transformer architecture.\n\n## 2. Introduction\n\nThe term \"llm\" has multiple meanings, but in the context of AI, it refers to Large Language Model. Understanding what LLM stands for and its applications is crucial in the field of natural language processing (NLP). LLMs have become a foundational technology behind modern chatbots and are used for various tasks such as generating, summarizing, translating, and analyzing text.\n\n## 3. Latest Findings\n\nThe latest information on LLMs indicates that they are typically based on transformer architecture, with generative pre-trained transformers (GPTs) being a type of LLM. Notable LLMs include BERT, GPT-1, GPT-2, GPT-3, and GPT-4. Additionally, open-weight LLMs and multimodal LLMs have been developed, allowing for more permissive usage and deployment.\n\n## 4. Key Developments\n\nThe development of LLMs has been rapid, with the first transformer-based models emerging in 2017. Since then, there have been significant advancements in the field, including the introduction of GPTs and the development of open-weight and multimodal LLMs. Tokenization is a crucial step in preparing text data for LLMs, with algorithms like byte-pair encoding (BPE) and WordPiece being used to convert text to numerical tokens.\n\n## 5. Evidence and Analysis\n\nThe evidence from the sources indicates that LLMs are a type of language model that utilizes the Transformer architecture to predict and generate natural language. The analysis of the sources suggests that LLMs have become a crucial technology in the field of NLP, with applications in chatbots, text generation, and language translation.\n\n## 6. Challenges and Limitations\n\nOne of the limitations of the research is that the term \"llm\" has multiple meanings, and it is essential to clarify the context in which it is being used. Additionally, the development of LLMs is a rapidly evolving field, and it is crucial to stay up-to-date with the latest advancements and developments.\n\n## 7. Conclusion\n\nIn conclusion, the research question \"llm\" is answered by defining what LLM stands for and its meaning in the context of AI. LLM stands for Large Language Model, which is a type of language model trained on massive amounts of text to predict and generate natural language.\n\n## 8. Sources\n\n* https://en.wikipedia.org/wiki/Large_language_model\n* https://llm-guide.com/what-is-an-llm\n* https://keymakr.com/blog/llm-meaning-what-does-the-abbreviation-llm-stand-for-in-ai-a-comprehensive-explanation\n\nNote: The source https://www.cloudflare.com/learning/ai/what-is-large-language-model was not directly relevant to the research question and required JavaScript and cookies to be enabled to access the content."
```

The agent searches relevant sources, processes the information, and generates a research-oriented response.

---

# 🎯 Use Cases

The AI Research Agent can be used for:

* 📚 Academic research
* 🧑‍💻 Technical research
* 📰 Latest technology research
* 🤖 AI/ML research
* 📊 Market research
* 🔎 Topic exploration
* 📝 Research report generation
* 🌐 Web-based information gathering
* 📖 Learning and knowledge discovery

---

# 🔐 Environment Variables

## Backend

```env
GROQ_API_KEY=
TAVILY_API_KEY=
```

## Frontend

```env
VITE_BACKEND_URL=
```

---


