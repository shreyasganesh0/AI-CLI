import os
import sys
from dotenv import load_dotenv
from google import genai

def prompt():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"

    if len(sys.argv) != 2 :

        print("Invalid arguments passed", sys.argv)
        sys.exit(1)

    prompt = sys.argv[1]

    resp = client.models.generate_content(model = model, contents = prompt)

    print(f"{resp.text}\nPrompt tokens: {resp.usage_metadata.prompt_token_count}\nResponse tokens:{resp.usage_metadata.candidates_token_count}\n")


if __name__ == "__main__":

    prompt()

