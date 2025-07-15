import faiss
import numpy as np
from embeddings import chunk_function, read_doc, embedding_function

document_path = r"C:\Users\DELL\Downloads\guru pornima.txt"
text = read_doc(document_path)
chunked_data = chunk_function(text)
embedded_func = embedding_function(chunked_data)

# Convert list of lists (embedding vectors) into a NumPy array
vectors_np = np.array(embedded_func).astype('float32')

# Get the dimensionality of the vectors (usually 1536 for OpenAI models)
dimension = vectors_np.shape[1]

# Create a FAISS index using L2 distance (Euclidean)
index = faiss.IndexFlatL2(dimension)

# Add all vectors to the index
index.add(vectors_np)

print("✅ Embeddings stored in FAISS index.")
print(f"📦 Total vectors in index: {index.ntotal}")
stored_vectors = index.reconstruct_n(0, index.ntotal)
print(stored_vectors[0])