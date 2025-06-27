import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def prompt():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"

    if len(sys.argv) < 2 :

        print("Invalid arguments passed", sys.argv)
        sys.exit(1)

    prompt = sys.argv[1]

    v_flag = False
    if len(sys.argv) == 3: 
        if sys.argv[2] == "--verbose":

            v_flag = True
        else:
            print("Invalid arguments passed", sys.argv)
            sys.exit(1)

    messages = [types.Content(role = "user", parts = [types.Part(text = prompt)])]

    resp = client.models.generate_content(model = model, contents = messages)

    print(f"{resp.text}\n")


    if v_flag == True:
        print(f"User prompt: {prompt}\n" 
              f"Prompt tokens: {resp.usage_metadata.prompt_token_count}\n" 
              f"Response tokens:{resp.usage_metadata.candidates_token_count}\n")


if __name__ == "__main__":

    prompt()

