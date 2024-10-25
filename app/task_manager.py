import os
import re
from datetime import datetime
from .code_synthesizer import generate_code  # Ensure this exists in code_synthesizer.py
from .file_manager import save_code_to_file  # Ensure this matches your file structure

def sanitize_filename(task):
    task_file_map = {
        "main application file": "app.py",
        "models": "models.py",
        "routes": "routes.py",
        "database connection": "database.py",
        "configuration file": "config.py"
    }
    
    for key, filename in task_file_map.items():
        if key in task.lower():
            return filename.replace(".py", f"_{datetime.now().strftime('%Y%m%d%H%M%S')}.py")
    
    base_name = re.sub(r'\W+', '_', task)[:20]
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{base_name}_{timestamp}.py"

def save_code_to_file(task, code):
    directory = "generated_code/"
    os.makedirs(directory, exist_ok=True)
    
    file_name = sanitize_filename(task)
    file_path = os.path.join(directory, file_name)

    with open(file_path, "w") as f:
        f.write(code)
    return file_path

def decompose_task(prompt):
    if "web app" in prompt.lower():
        return [
            "Create a main application file (app.py) with Flask setup",
            "Create models for the application",
            "Create routes for the application",
            "Set up a database connection",
            "Write a configuration file",
        ]
    return [prompt]

def handle_task(prompt):
    tasks = decompose_task(prompt)
    responses = []

    for task in tasks:
        code = generate_code(task)
        file_path = save_code_to_file(task, code)
        responses.append({"task": task, "file_path": file_path, "code": code})
    
    return {"tasks": tasks, "responses": responses}
