from tools.pdf_reader import extract_text_from_pdf
from tools.text_chunker import chunk_text
from tools.embeddings import generate_embeddings
from tools.vector_store import create_faiss_index, retrieve_chunks
from tools.web_search import search_web
from tools.llm import generate_response

# PDF PIPELINE
pdf_text = extract_text_from_pdf("sample.pdf")
chunks = chunk_text(pdf_text)
embeddings = generate_embeddings(chunks)
index = create_faiss_index(embeddings)

query = "What are Pranav's ML projects?"

# --- PDF retrieval ---
query_embedding = generate_embeddings([query])[0]
pdf_chunks = retrieve_chunks(query_embedding, index, chunks, top_k=3)
pdf_context = "\n".join(pdf_chunks)

# --- WEB retrieval ---
web_context = search_web(query)

# --- FINAL ANSWER ---
answer = generate_response(query, pdf_context, web_context)

print("\nFINAL ANSWER:\n")
print(answer)