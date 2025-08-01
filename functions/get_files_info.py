from pathlib import Path

def get_files_info(working_directory, directory=None):

    try:

        parent = Path(working_directory).resolve()

        child = Path()
        if directory[0] != '/':
            child = Path(working_directory + '/' + file_path).resolve()
        else:
            child = Path('/' + file_path).resolve()
    except Exception as e:

        return f'Error resolving path: {e}'

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

