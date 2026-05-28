import os
import argparse
from tools.pdf_reader import extract_text_from_pdf
from tools.text_chunker import chunk_text
from tools.embeddings import generate_embeddings
from tools.vector_store import create_faiss_index, retrieve_chunks
from tools.web_search import search_web
from tools.llm import generate_response

def main():
    parser = argparse.ArgumentParser(description="Hybrid AI Research Assistant")
    parser.add_argument("query", type=str, help="Research query to ask the AI")
    parser.add_argument("--pdf", type=str, default=None, help="Optional path to a PDF file for document context")
    args = parser.parse_args()

    query = args.query
    pdf_path = args.pdf

    # Initialize context
    pdf_context = "Not provided"

    # --- 1. WEB RETRIEVAL (PRIMARY) ---
    print(f"Searching web for: {query}")
    web_context = search_web(query)

    # --- 2. PDF RETRIEVAL (OPTIONAL) ---
    if pdf_path:
        if os.path.exists(pdf_path):
            print(f"Extracting context from PDF: {pdf_path}")
            pdf_text = extract_text_from_pdf(pdf_path)
            
            if pdf_text and pdf_text.strip():
                chunks = chunk_text(pdf_text)
                if chunks:
                    embeddings = generate_embeddings(chunks)
                    index = create_faiss_index(embeddings)
                    
                    query_embedding = generate_embeddings([query])[0]
                    pdf_chunks = retrieve_chunks(query_embedding, index, chunks, top_k=3)
                    pdf_context = "\n\n---\n\n".join(pdf_chunks)
            else:
                print("Warning: PDF was empty or could not be read.")
        else:
            print(f"Warning: PDF file not found at {pdf_path}")
    else:
        print("No PDF provided. Proceeding with Web context only.")

    # --- 3. GENERATE FINAL RESPONSE ---
    print("\nGenerating AI Response...")
    answer = generate_response(query, pdf_context, web_context)

    print("\n================ FINAL ANSWER ================\n")
    print(answer)

if __name__ == "__main__":
    main()
