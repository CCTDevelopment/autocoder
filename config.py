import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or "your_openai_api_key_here"
    TASK_LIMIT = 5  # Limit number of recursive tasks to avoid infinite loops
