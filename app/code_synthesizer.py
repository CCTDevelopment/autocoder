import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def generate_code(prompt):
    modified_prompt = f"Write only the code. {prompt}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a coding assistant that provides only code output."},
                {"role": "user", "content": modified_prompt}
            ],
            max_tokens=150
        )
        code = response['choices'][0]['message']['content'].strip()
        return code
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return None
