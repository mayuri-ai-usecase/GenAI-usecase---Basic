import os
#from openai import OpenAI
from docx import Document

#connect api key with python code
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#get document
document_path = r"C:\Users\DELL\Downloads\guru pornima.txt"

#Reading function
def read_doc(document_path):
    #below code was for .doc file
    '''doc=Document(document_path)
    full_test = "\n".join(para.text for para in doc.paragraphs if para.text.strip()!="")
    return full_test'''

    #below code is for .txt file
    with open(document_path, "r", encoding="utf-8") as file:
        text=file.read()
    return text

#text = read_doc(document_path)
#print(text[:300])

#Chunking of data
def chunk_function(text, chunk_size=200, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap
    #print(f"\nTotal chunks generated: {len(chunks)}")
    return chunks

#chunked_data = chunk_function(text)
#print(f"length of chunked_data {chunked_data}")