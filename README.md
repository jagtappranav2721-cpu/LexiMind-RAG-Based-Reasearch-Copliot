LexiMind AI – RAG-Based Research Copilot
LexiMind AI is a hybrid research assistant that accelerates the information-gathering process by combining real-time web search, document parsing (PDF), and Large Language Models (LLMs).

Unlike standard chatbots that rely solely on pre-trained knowledge, LexiMind utilizes a Retrieval-Augmented Generation (RAG) pipeline to fetch relevant context first, ensuring responses are accurate, grounded, and structurally formatted for research workflows.

📌 Overview
This system simulates a real-world AI research workflow:

Ingest: Takes a user query and optional PDF documents.

Retrieve: Extracts text, chunks it, and performs semantic search via FAISS alongside real-time web search.

Synthesize: Passes the augmented context to an LLM to generate a structured, factual response.

Export: Allows users to download the final analysis as a formatted PDF report.

✨ Key Features
Hybrid RAG Pipeline: Seamlessly merges web search results with local document retrieval for comprehensive context.

Document Understanding: Automatically extracts, chunks, and embeds text from user-uploaded PDFs using FAISS and Sentence Transformers.

Context-Aware Synthesis: Prevents AI hallucinations by forcing the LLM to generate answers strictly based on the retrieved vector embeddings.

Automated Report Generation: Converts the final AI output into a clean, downloadable PDF report (via ReportLab) for offline use.

Interactive UI: A lightweight, responsive frontend built with Streamlit for rapid prototyping and easy interaction.

🏗️ Architecture & Workflow
User Query 
 ├──> Web Search (DuckDuckGo API for real-time context)
 └──> Document Upload (PDF)
       └──> Text Extraction -> Chunking -> FAISS Vector Store
              └──> Similarity Search (Semantic Retrieval)
                      │
                      V
             Context Assembly
                      │
                      V
           OpenRouter (DeepSeek LLM)
                      │
                      V
         Structured Final Response 
         (Optional: Export to PDF)

🛠️ Tech Stack
Language: Python

Frontend: Streamlit

Vector Database: FAISS (Facebook AI Similarity Search)

Embeddings: Sentence Transformers

LLM Provider: OpenRouter (DeepSeek)

APIs & Utilities: DuckDuckGo Search API, ReportLab (PDF generation)

🚀 Getting Started
Prerequisites
Python 3.8+

An active OpenRouter API Key

Installation
Clone the repository:

Bash
git clone https://github.com/jagtappranav2721-cpu/leximind-ai.git
cd leximind-ai
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory and add your OpenRouter API key:

Code snippet
OPENROUTER_API_KEY=your_api_key_here
Run the application:

Bash
streamlit run app.py
🎯 Use Cases
Academic & Technical Research: Quickly synthesize information from multiple research papers.

Document Q&A: Chat directly with heavy PDF manuals or reports.

Automated Briefings: Generate rapid, well-researched summaries on current events or specific topics.

🗺️ Roadmap
[ ] Streaming Responses: Implement token-by-token streaming for lower perceived latency.

[ ] Multi-Document Support: Allow batch uploading and querying across multiple PDFs simultaneously.

[ ] Citation Tracking: Map LLM claims back to specific chunks/pages in the source document.

[ ] Advanced Retrieval: Implement hybrid search (keyword + semantic) for better source ranking.

[ ] UI Overhaul: Migrate the frontend to a React/Next.js stack for enhanced state management and component design.

👨‍💻 Author
Pranav Jagtap GitHub: jagtappranav2721-cpu

         
