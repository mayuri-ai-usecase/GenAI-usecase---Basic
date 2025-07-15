from chunking_data import read_doc, chunk_function
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

document_path = r"C:\Users\DELL\Downloads\guru pornima.txt"
text = read_doc(document_path)
chunked_data = chunk_function(text)

def embedding_function(chunks, model="text-embedding-3-small"):
    embeddings = []

    for i, chunk in enumerate(chunks):
        response = client.embeddings.create(
            input=chunk,
            model=model
        )

        vector = response.data[0].embedding

        embeddings.append(vector)

        #print(f"embedded chunk : {vector}")

    return embeddings

#embedded_func = embedding_function(chunked_data)