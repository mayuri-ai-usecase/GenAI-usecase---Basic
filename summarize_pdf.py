import os
from openai import OpenAI
import PyPDF2

#connect with api-key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#provide pdf path
file_path = r"C:\Users\DELL\Downloads\Randstad Experience letter.pdf"

#read data from pdf
with open(file_path, "rb"):
    reader = PyPDF2.PdfReader(open(file_path, "rb"))
    pdf_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

#ask question
#question = input("ask your question..")

# Step 2: Continuous Q&A loop
print("🔎 Ask any question based on the PDF. Type 'exit' or 'stop' to end.\n")

while True:
    question = input("your question ?\n")

    if question.lower() in "exit":
        print("session ended, see you next time")
        break

    #use gpt model to summarize data
    response = client.chat.completions.create(
        model="gpt-4o",
        messages = [
            {
            "role" : "user",
            # "content" : f"summarize the pdf in 2 lines. \n\n {pdf_text}"
            "content" : f"give the answer from the pdf \n\n{pdf_text} on asked question \n\n{question}"
            }
        ]
    )

    #print response
    print("\n💡 Answer:")
    print(response.choices[0].message.content)
    print("\n" + "-" * 60 + "\n")





