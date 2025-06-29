from pathlib import Path

def write_file(working_directory, file_path, content):

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




