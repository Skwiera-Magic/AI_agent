import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python file in relative working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to run function from, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Command-line argument to pass to the Python script",
                ),
                description="Command-line arguments to pass to the Python script",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args is not None:
            command.extend(args)
        completed = subprocess.run(command, cwd=working_directory, capture_output=True, text=True,timeout=30)
        output = ""
        if completed.returncode != 0:
            output += f"Process exited with code {completed.returncode}"
        if completed.stdout != "":
            output += f"\nSTDOUT: {completed.stdout}"
        if completed.stderr != "":
            output += f"\nSTDERR: {completed.stderr}"
        if completed.stdout == "" and completed.stderr == "":
            output += f"No output produced"
        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"