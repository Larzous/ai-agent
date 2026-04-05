import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    if api_key is None:
        raise RuntimeError("Missing Gemini API Key")
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
