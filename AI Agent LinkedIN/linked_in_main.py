import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load OpenAI API key from .env file
load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")

# 🚀 Setup GPT-4o chat model via LangChain
llm = ChatOpenAI(
    openai_api_key=open_api_key,
    model_name="gpt-4o",
    temperature=0.7
)

# ✏️ Prompt template for structured LinkedIn-style posts
template = PromptTemplate(
    input_variables=["topic"],
    template="""
You are a LinkedIn content expert. Create an engaging post on the topic: "{topic}"

- Write 3–5 sentences
- Use a professional but warm tone
- Encourage reflection or interaction
- Avoid hashtags
- Add one related image on the topic
"""
)

# 📝 Function to generate post using LangChain
def generate_post_langchain(topic):
    prompt = template.format(topic=topic)
    response = llm.predict(prompt)
    return response

#moved this code to main.py
"""# 🔁 Run this file directly to test
if __name__ == "__main__":
    print("\n📣 Welcome to the AI LinkedIn Post Generator!")
    topic = input("📝 Please enter the topic for your post: ")
    print("\n💡 Generating post for topic:", topic)
    post = generate_post_langchain(topic)
    
    print("\n🟢 Generated LinkedIn Post:\n")
    print(post)"""