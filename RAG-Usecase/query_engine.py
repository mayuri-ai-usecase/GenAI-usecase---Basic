from embeddings import chunk_function, read_doc, embedding_function
from chunking_data import chunk_function
from save_embedding_to_Faiss_db import index, chunked_data
from openai import OpenAI
import numpy as np
import os

# Initialize OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_query(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    vector = response.data[0].embedding
    return np.array(vector).astype("float32").reshape(1, -1)

def retrieve_top_chunks(query, top_k=5):
    # Step 1: Optional chunking if query is long
    if len(query.split()) > 100:
        query_chunks = chunk_function(query)
        query = " ".join(query_chunks)  # Simplify: merge chunks

    # Step 2: Embed the query
    query_vector = embed_query(query)

    # Step 3: Search FAISS index
    distances, indices = index.search(query_vector, top_k)

    # Step 4: Map indices to original chunks
    matched_chunks = [chunked_data[i] for i in indices[0]]
    return matched_chunks

while True:
    user_question = input("\n❓ Ask a question (or type 'exit' to quit): ")

    if user_question.lower() == "exit":
        print("👋 Session ended. Have a great day!")
        break

    results = retrieve_top_chunks(user_question)

     # 👇 Replace this block…
    # print("\n🔍 Top matching chunks:")
    # for i, chunk in enumerate(results):
    #     print(f"\n📄 Chunk {i+1}:\n{chunk[:400]}...\n")

    # 👇 With GPT-4o answer generation
    context = "\n\n".join(results)
    prompt = f"""
    Use the following context to answer the question clearly and accurately:

    Context:
    {context}

    Question:
    {user_question}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content
    print(f"\n💬 Answer:\n{answer}")
