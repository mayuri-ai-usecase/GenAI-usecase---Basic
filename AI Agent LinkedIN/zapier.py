import os
import requests
from dotenv import load_dotenv
print("Zapier file started")
load_dotenv(dotenv_path="constants.env")


ZAPIER_WEBHOOK_URL = os.getenv("ZAPIER_WEBHOOK_URL") 


def send_post_to_zapier(post_text):
    payload = {"linkedin_post": post_text}
    response = requests.post(ZAPIER_WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print("✅ Successfully sent post to Zapier!")
    else:
        print(f"⚠️ Error {response.status_code}: {response.text}")

