import subprocess

def validate_code(file_path):
    """Run a basic syntax check on the code."""
    try:
        result = subprocess.run(["python3", "-m", "py_compile", file_path], capture_output=True, text=True)
        if result.returncode == 0:
            return "Syntax OK"
        else:
            return f"Syntax Error: {result.stderr}"
    except Exception as e:
        return f"Error during validation: {e}"
