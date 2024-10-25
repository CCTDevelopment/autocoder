import os
import re
from datetime import datetime

def sanitize_filename(prompt):
    # Replace spaces and special characters with underscores, truncate to 20 characters
    base_name = re.sub(r'\W+', '_', prompt)[:20]
    # Append a timestamp to make it unique
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{base_name}_{timestamp}.py"

def save_code_to_file(prompt, code):
    directory = "generated_code/"
    os.makedirs(directory, exist_ok=True)
    
    # Sanitize the file name based on the prompt
    file_name = sanitize_filename(prompt)
    file_path = os.path.join(directory, file_name)

    with open(file_path, "w") as f:
        f.write(code)
    return file_path  # Return file path for confirmation or logging
