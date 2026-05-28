import streamlit as st
import os
from tools.pdf_reader import extract_text_from_pdf
from tools.text_chunker import chunk_text
from tools.embeddings import generate_embeddings
from tools.vector_store import create_faiss_index, retrieve_chunks
from tools.web_search import search_web
from tools.llm import generate_response
from tools.pdf_generator import generate_professional_pdf
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="AI Research Copilot", page_icon="✨", layout="wide")

st.title("✨LexiMind AI")

# Hide streamlit default styling to make it cleaner
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I am your AI Research Assistant. What would you like to research today?"}]

# Display chat messages from history on app rerun
for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Display the PDF download button for past assistant messages if it exists
        if "pdf_path" in message and os.path.exists(message["pdf_path"]):
            with open(message["pdf_path"], "rb") as pdf_file_obj:
                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf_file_obj,
                    file_name=os.path.basename(message["pdf_path"]),
                    mime="application/pdf",
                    key=f"download_{idx}"
                )

# ---------------------------------------------------------
# INPUT SECTION (BOTTOM)
# ---------------------------------------------------------
st.markdown("---")

col_input, col_upload, col_btn = st.columns([5, 2, 1])

with col_input:
    prompt = st.text_input("Ask a research question...", key="search_input", label_visibility="collapsed", placeholder="Enter your research query...")
    
with col_upload:
    pdf_file = st.file_uploader("Upload PDF", type=["pdf"], label_visibility="collapsed")
    
with col_btn:
    search_clicked = st.button("Search", type="primary", use_container_width=True)

# Process PDF if uploaded
if pdf_file:
    if "pdf_name" not in st.session_state or st.session_state.pdf_name != pdf_file.name:
        with st.spinner("Processing document..."):
            with open("temp.pdf", "wb") as f:
                f.write(pdf_file.read())
            
            text = extract_text_from_pdf("temp.pdf")
            if text and text.strip():
                st.session_state.chunks = chunk_text(text)
                st.session_state.embeddings = generate_embeddings(st.session_state.chunks)
                st.session_state.index = create_faiss_index(st.session_state.embeddings)
                st.session_state.pdf_name = pdf_file.name
                st.success("✅ Document indexed!")
            else:
                st.error("Failed to extract text.")
else:
    st.session_state.pop("chunks", None)
    st.session_state.pop("index", None)
    st.session_state.pop("pdf_name", None)

# Execute search
if search_clicked and prompt:
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            web_context = search_web(prompt)
            pdf_context = "Not provided"
            
            if "index" in st.session_state and st.session_state.index is not None:
                query_embedding = generate_embeddings([prompt])[0]
                results = retrieve_chunks(query_embedding, st.session_state.index, st.session_state.chunks, top_k=3)
                if results:
                    pdf_context = "\n\n---\n\n".join(results)

            try:
                answer = generate_response(prompt, pdf_context, web_context)
                
                # Directly output the answer
                st.markdown(answer)
                
                # Generate Professional PDF
                pdf_path = generate_professional_pdf(prompt, answer, web_context, pdf_context)
                
                # Show Download button
                with open(pdf_path, "rb") as pdf_file_obj:
                    st.download_button(
                        label="📄 Download PDF Report",
                        data=pdf_file_obj,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf",
                        key=f"download_new_{len(st.session_state.messages)}"
                    )
                
                # Add assistant response to chat history
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": answer,
                    "pdf_path": pdf_path
                })
                
            except Exception as e:
                error_msg = f"An error occurred while generating the response: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})