from pathlib import Path
import subprocess

def run_python_file(working_directory, file_path, **kwargs):

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

            return f'Error: File "{child.resolve()}" not found.'

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
        
        if not result.stdout.strip() and not result.stderr.strip():

            return "No output produced"

        if result.returncode != 0:

            return f"Process exited with code {result.resultcode}" 

        res = "STDOUT:\n"
        for line in result.stdout.splitlines():
            res += (f"{line}")

        res = "STDERR:\n"
        for line in result.stderr.splitlines():
            res += (f"{line}")
        return res

    except subprocess.CalledProcessError as e:

        return res + f"Error: executing Python file: {e}"

    
    
def get_files_info(working_directory, directory=None, **kwargs):

    try:

        parent = Path(working_directory).resolve()

        child = Path()
        if directory[0] != '/':
            child = Path(working_directory + '/' + directory).resolve()
        else:
            child = Path('/' + directory).resolve()
    except Exception as e:

        return f'Error resolving path: {e}'

    print(child.resolve())

    try:

        child.relative_to(parent)
    except ValueError:

        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not child.is_dir():

        return f'Error: "{directory}" is not a directory'

    ret_str = f""
    for item in child.iterdir():

        size = item.stat().st_size
        is_dir = item.is_dir()
        ret_str += f'- {item.name}: file_size={size} bytes, is_dir={is_dir}\n'

    return ret_str

def write_file(working_directory, file_path, content, **kwargs):

    try:

        parent = Path(working_directory).resolve()

        child = Path()
        if file_path[0] != '/':
            child = Path(working_directory + '/' + file_path).resolve()
        else:
            child = Path(file_path).resolve()
    except Exception as e:

        return f'Error resolving path: {e}'

    try:

        child.relative_to(parent)
    except ValueError:

        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    
    try:
        with child.open("w") as file:

            file.write(content)
    except Exception as e:

            return f'Error writing content to file{child.resolve()}: {e}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'





def get_file_content(working_directory, file_path, **kwargs):

    try:

        parent = Path(working_directory).resolve()

        child = Path()
        if file_path[0] != '/':
            child = Path(working_directory + '/' + file_path).resolve()
        else:
            child = Path(file_path).resolve()
    except Exception as e:

        return f'Error resolving path: {e}'


    try:

        child.relative_to(parent)
    except ValueError:

        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if child.is_dir():

        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(str(child.resolve()) , 'r') as file:

        contents = file.read(10000)
        next_char = file.read(1)
    
    if next_char:

        contents += f'[...File "{file_path}" truncated at 10000 characters]'

    return contents
