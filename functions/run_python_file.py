import subprocess
from pathlib import Path

def run_python_file(working_directory, file_path):

    if not file_path.endswith(".py"):

        return f'Error: "{file_path}" is not a Python file.'

    try:

        parent = Path(working_directory).resolve()

        child = Path()
        if file_path[0] != '/':
            child = Path(working_directory + '/' + file_path).resolve()
        else:
            child = Path(file_path).resolve()

        if not child.exists():

            return f'Error: File "{file_path}" not found.'

    except Exception as e:

        return f'Error resolving path: {e}'

    try:

        child.relative_to(parent)
    except ValueError:

        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    try:
        result = subprocess.run(["python3", str(child.resolve())],
                             timeout = 30,
                             capture_output = True,
                             text = True,
                             cwd = working_directory) 
        
        if not result.stdout.strip():

            return "No output produced"

        if result.returncode != 0:

            return f"Process exited with code {result.resultcode}" 

        res = "STDOUT:\n"
        for line in result.stdout.splitlines():
            res += (f"{line}")
        return res

    except subprocess.CalledProcessError as e:

        res = "STDERR:\n"
        for line in result.stderr.splitlines():
            res += (f"{line}")
        return res + f"Error: executing Python file: {e}"

    
    
