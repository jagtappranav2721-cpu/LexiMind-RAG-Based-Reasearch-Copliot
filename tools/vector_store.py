import faiss
import numpy as np


def create_faiss_index(embeddings):

    # Convert embeddings into float32
    embeddings = np.array(
        embeddings
    ).astype('float32')

    # FAIL FAST: Prevent creating a 0-dimensional FAISS index
    if embeddings.size == 0:
        raise ValueError("Cannot create FAISS index: embeddings array is empty (no chunks provided).")

    # Reshape only if single vector
    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    print("\nEmbeddings Shape:")
    print(embeddings.shape)

    # Get embedding dimension
    dimension = embeddings.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatL2(
        dimension
    )

    # Add embeddings
    index.add(embeddings)

    return index


def retrieve_chunks(
    query_embedding,
    index,
    chunks,
    top_k=1
):
    if index.ntotal == 0 or len(chunks) == 0:
        return []

    # Convert query embedding into float32
    query_embedding = np.array(
        query_embedding
    ).astype('float32')

    # Reshape ONLY if single vector
    if query_embedding.ndim == 1:
        query_embedding = query_embedding.reshape(1, -1)

    print("\nQuery Shape:")
    print(query_embedding.shape)

    print("\nFAISS Dimension:")
    print(index.d)

    # VALIDATE dimensions to prevent obscure FAISS AssertionError
    if query_embedding.shape[1] != index.d:
        raise ValueError(
            f"Dimension mismatch! Query embedding has {query_embedding.shape[1]} dimensions, "
            f"but FAISS index was created with {index.d} dimensions."
        )

    # Search similar vectors
    distances, indices = index.search(
        query_embedding,
        top_k
    )

    # Retrieve chunks
    retrieved_chunks = [
        chunks[i]
        for i in indices[0] if i != -1 and i < len(chunks)
    ]

    return retrieved_chunks