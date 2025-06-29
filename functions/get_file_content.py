from pathlib import Path

def get_file_content(working_directory, file_path):

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



