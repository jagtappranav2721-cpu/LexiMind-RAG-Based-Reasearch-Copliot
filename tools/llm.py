from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = os.getenv("OPENROUTER_API_KEY")
)

def generate_response(query, pdf_context, web_context):

    prompt = f"""
You are a highly capable AI Research Assistant (similar to Perplexity).
Your goal is to answer the user's research query comprehensively and accurately.

=====================
WEB CONTEXT (PRIMARY SOURCE):
{web_context}

=====================
PDF CONTEXT (OPTIONAL/SECONDARY SOURCE):
{pdf_context}

=====================
User Question:
{query}

Instructions:
1. Prioritize WEB_CONTEXT for general knowledge and factual answers.
2. Use PDF_CONTEXT ONLY if it is relevant (e.g. for user-specific or uploaded content). If it says "Not provided", ignore it.
3. If there is a conflict between the web and the PDF, explicitly mention both sources and explain the discrepancy.
4. Output STRICTLY in this markdown format:
   ## Executive Summary
   [Short 3-5 line summary]
   ## Detailed Analysis
   [Well formatted paragraphs explaining the findings]
   ## Key Insights
   [Bullet points of important insights]
   ## Conclusion
   [Final summary of findings]
"""

    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content