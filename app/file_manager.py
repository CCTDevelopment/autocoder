import logging
import os

def save_code_to_file(file_name, code):
    try:
        directory = "generated_code/"
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, file_name)

        with open(file_path, "w") as f:
            f.write(code)
        
        logging.info("Code saved to file: %s", file_path)
        return file_path
    except Exception as e:
        logging.error("Error saving file %s: %s", file_name, e)
        return None
