from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
embedding_model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)


def generate_embeddings(chunks):
    # 1) Handle empty input gracefully to prevent shape (0,) issues
    if not chunks:
        return np.array([]).astype('float32')

    # 2) Ensure chunks is always a list
    if isinstance(chunks, str):
        chunks = [chunks]

    # 3) Generate embeddings
    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True
    )

    # 4) Convert to float32
    embeddings = np.array(
        embeddings
    ).astype('float32')

    # 5) Ensure 2D shape (N, D) in case a single string was encoded
    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    return embeddings