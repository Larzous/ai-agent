import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    if api_key == None:
        raise RuntimeError("Missing Gemini API Key")
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
