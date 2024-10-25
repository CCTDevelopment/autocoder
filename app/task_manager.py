import logging
import os
import re
from datetime import datetime
from app.code_synthesizer import generate_code
from app.file_manager import save_code_to_file

def sanitize_filename(task_description):
    task_file_map = {
        "main application file": "app.py",
        "models": "models.py",
        "routes": "routes.py",
        "configuration file": "config.py"
    }

    for key, filename in task_file_map.items():
        if key in task_description.lower():
            return filename

    base_name = re.sub(r'\W+', '_', task_description)[:20]
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{base_name}_{timestamp}.py"

def decompose_task(prompt):
    if "web app" in prompt.lower():
        return [
            {"description": "Create the main Flask application entry point (app.py) with Flask setup, configuration loading from config.py, database initialization, and blueprint registration for routes.", "file_name": "app.py"},
            {"description": "Create SQLAlchemy models for the application in models.py, including a User model with fields for id, username, email, and password.", "file_name": "models.py"},
            {"description": "Create routes for user authentication in routes.py using Flask Blueprints. Include routes for /register and /login, and ensure this blueprint is imported and registered in app.py.", "file_name": "routes.py"},
            {"description": "Set up the database configuration file config.py with SQLAlchemy URI and secret key, ensuring app.py imports it for app configuration.", "file_name": "config.py"}
        ]
    return [{"description": prompt, "file_name": sanitize_filename(prompt)}]

def handle_task(prompt):
    tasks = decompose_task(prompt)
    responses = []

    for task in tasks:
        try:
            logging.info("Generating code for task: %s", task["description"])
            code = generate_code(task["description"])

            if not code:
                logging.warning("Code generation returned empty for task '%s'", task["description"])
                continue

            file_path = save_code_to_file(task["file_name"], code)
            
            if file_path:
                logging.info("Code saved for task '%s' at %s", task["description"], file_path)
                responses.append({"task": task["description"], "file_path": file_path, "code": code})
            else:
                logging.error("Failed to save code for task '%s'", task["description"])
        
        except Exception as e:
            logging.error("Error handling task '%s': %s", task["description"], e)

    return {"tasks": tasks, "responses": responses}
