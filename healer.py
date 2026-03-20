import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def fix_my_code(error_message, source_code):

    prompt = f"""
    You are an expert software engineer. A Python script failed.
    ERROR: {error_message}
    ORIGINAL CODE:
    {source_code}

    TASK: Fix the code. 
    CONSTRAINTS: Return ONLY the raw code. No markdown code blocks (```), no explanations.
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text.strip()

if __name__ == "__main__":

    # 1. read the broken file
    with open("processor.py", "r") as f:
        broken_code = f.read()
    
    # 2. read error log
    with open("error.log", "r") as log:
        error_data = json.load(log)
    
    error_message = f"{error_data['type']}: {error_data['message']}"

    # 3. get the fix
    fixed_code = fix_my_code(error_message, broken_code)
    
    # 4. overwrite the file with the fix
    with open("processor.py", "w") as f:
        f.write(fixed_code)