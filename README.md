🧠 LexiMind AI — RAG-Based Research Copilot

A Hybrid AI Research Assistant that combines Web Search + PDF Intelligence + LLM Reasoning to generate structured, citation-style research answers with downloadable reports.

🚀 What is this project?

LexiMind AI is an intelligent research copilot that helps users get well-structured, context-aware answers by combining:

🌐 Real-time web search (DuckDuckGo)
📄 PDF document understanding (RAG pipeline)
🧠 Vector-based semantic retrieval (FAISS)
🤖 LLM reasoning (DeepSeek via OpenRouter)
📥 Auto-generated PDF reports

Instead of just giving chatbot responses, LexiMind behaves like a mini research engine that gathers, filters, and synthesizes information.

🎯 Why I built this

Most chatbots either:

only use static training data ❌
or don’t understand user documents properly ❌

I wanted to build something closer to real-world tools like Perplexity AI / NotebookLM, where:

AI doesn’t just answer — it researches before answering.

⚙️ Key Features
🔍 Hybrid RAG System
Combines PDF knowledge + web search + LLM reasoning
Context-aware responses using semantic retrieval
📄 PDF Intelligence
Upload any document
Extracts + chunks text automatically
Uses FAISS for fast similarity search
🌐 Real-Time Web Research
Fetches live information from the web
Improves accuracy with up-to-date context
🧠 LLM-Powered Reasoning
Uses DeepSeek via OpenRouter API
Structured, human-like research answers
📊 Smart Response Formatting

Each answer includes:

Summary
Detailed explanation
Key insights
Source references
📥 Downloadable Reports
Generates professional PDF reports
Useful for assignments, research work, or documentation
💻 Interactive UI
Built with Streamlit
Clean chat-like interface
Fast experimentation workflow
🏗️ System Architecture
User Query
   ↓
Web Search ─────┐
                ├── Context Fusion ──→ LLM (DeepSeek)
PDF (FAISS) ────┘
   ↓
Final Structured Answer
   ↓
PDF Report Generator
🧰 Tech Stack
Python
Streamlit (UI)
FAISS (Vector Search)
SentenceTransformers (Embeddings)
DuckDuckGo Search API
OpenRouter API (DeepSeek LLM)
ReportLab (PDF generation)
PyTorch / Transformers
📦 Installation
git clone https://github.com/your-username/leximind-ai.git
cd leximind-ai

pip install -r requirements.txt
🔐 Environment Variables

Create a .env file:

OPENROUTER_API_KEY=your_api_key_here
▶️ Run the App
streamlit run app.py
💡 Example Use Cases
📚 Academic research summaries
🧾 Assignment/report generation
🔍 Fast topic understanding
📄 PDF-based Q&A
🌐 Real-time web research assistant
📊 What makes this different?

Unlike basic chatbots, LexiMind AI:

✔ Uses real retrieval (not just prompts)
✔ Grounds answers in documents + web data
✔ Produces structured research outputs
✔ Generates downloadable reports
✔ Works like a mini AI research engine

📌 Future Improvements
Streaming response UI (ChatGPT-like typing)
Multi-document RAG support
Citation linking with sources
FastAPI backend upgrade
React frontend (production UI)
User authentication system
👨‍💻 Author

Pranav Jagtap

GitHub: https://github.com/jagtappranav2721-cpu
LinkedIn: www.linkedin.com/in/pranav-jagtap-065b39345
Email: jagtappranav2721@gmail.com
⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!
