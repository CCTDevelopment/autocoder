import openai
from config import Config  # Absolute import

openai.api_key = Config.OPENAI_API_KEY

def generate_code(prompt):
    modified_prompt = f"Write only the code. {prompt}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a coding assistant that provides only code output."},
                {"role": "user", "content": modified_prompt}
            ],
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return None
