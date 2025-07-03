from google.genai import types

from .helper_funcs import run_python_file, get_files_info, write_file, get_file_content

def call_function(func_call_specs, verbose=False):

    functions_dict = {

        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if verbose:
        print(f"Calling function: {func_call_specs.name}({func_call_specs.args})")
    else: 
        print(f" - Calling function: {func_call_specs.name}")
    

    WORKING_DIR = "./calculator"

    exec_function = functions_dict.get(func_call_specs.name, fall_back_func)

    resp = {}

    args_dict = {"working_directory": WORKING_DIR}
    args_dict.update(func_call_specs.args);
    args_dict["function_name"] = func_call_specs.name
    function_result = exec_function(**args_dict)

    if exec_function == fall_back_func:

        resp ={"error": function_result}

    else:
        resp = {"result": function_result}
    

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=func_call_specs.name,
                response=resp,
            )
        ],
    )

def fall_back_func(**kwargs):

    return f"Unknown function: {kwargs["function_name"]}"
