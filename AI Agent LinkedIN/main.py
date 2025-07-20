from linked_in_main import generate_post_langchain
from zapier import send_post_to_zapier

def run_ai_linkedin_agent():
    print("\n📣 Welcome to your AI LinkedIn Agent!")
    topic = input("📝 Enter the topic you'd like to post about: ")

    print("\n✨ Generating post with GPT-4o...")
    post = generate_post_langchain(topic)

    print("\n📝 Generated LinkedIn Post:\n")
    print(post)

    confirm = input("\n🚀 Would you like to auto-post this via Zapier? (yes/no): ").strip().lower()
    if confirm in ["yes", "y"]:
        send_post_to_zapier(post)
    else:
        print("❎ Skipped auto-posting. You can reuse this post manually.")

if __name__ == "__main__":
    run_ai_linkedin_agent()