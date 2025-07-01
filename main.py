import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def prompt():

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

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

    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    ) # tell the LLM what functions it can use

    resp = client.models.generate_content(model = model,
                                          contents = messages,
                                          config = types.GenerateContentConfig(
                                            tools=[available_functions], 
                                            system_instruction=system_prompt
                                            )
                                        )

    #print(f"{resp.text}\n")

    for func in resp.function_calls:
        print(f"Calling function: {func.name}({func.args})")


    if v_flag == True:
        print(f"User prompt: {prompt}\n" 
              f"Prompt tokens: {resp.usage_metadata.prompt_token_count}\n" 
              f"Response tokens:{resp.usage_metadata.candidates_token_count}\n")


if __name__ == "__main__":

    prompt()

