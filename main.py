import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function

from functions.schemas import (
    schema_get_files_info,
    schema_get_file_content,  
    schema_run_python_file,
    schema_write_file,
)

def prompt():

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

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

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_write_file,
            schema_run_python_file,
            schema_get_file_content,
        ]
    ) # tell the LLM what functions it can use

    for i in range(20):

        resp = client.models.generate_content(model = model,
                                              contents = messages,
                                              config = types.GenerateContentConfig(
                                                tools=[available_functions], 
                                                system_instruction=system_prompt
                                                )
                                            )
        if not resp.function_calls:

            print(f"Final Result: {resp.text}\n")
            break

        for candidate in resp.candidates:

            messages.append(candidate.content)


        for func in resp.function_calls:

            function_call_result = call_function(func, v_flag);
            
            messages.append(function_call_result)
            contents = function_call_result.parts[0].function_response.response
            if not contents:

                raise Exception(f"No response recieved for this function:\n{contents}")
            else:
                if v_flag == True:
                    print(f"-> {function_call_result.parts[0].function_response.response}\n")
                    print(f"User prompt: {prompt}\n" 
                          f"Prompt tokens: {resp.usage_metadata.prompt_token_count}\n" 
                          f"Response tokens:{resp.usage_metadata.candidates_token_count}\n")
                

if __name__ == "__main__":

    prompt()

