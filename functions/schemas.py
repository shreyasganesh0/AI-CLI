from google import genai
from google.genai import types

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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description = "Get the content for a given file if the file exists in the working directory path if it is a file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path for given file whose contents we want to list out if it exsists in the working directory and is a file.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python script with optinal arguments if the script is a .py file and if it exists within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the potential python script with optinal arguments to run if it is in the working directory and if it is a python script with a .py extension",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write and create or overwrite an exisitng file given by the file path if it exsits in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to create a new file or overwrite an existing file in if it points to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents that are to be written to the file. Only the first 10000 characters of contents will be written the remaining will be truncated.",
            ),
        },
    ),
)
