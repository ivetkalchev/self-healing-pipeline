import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-3-flash-preview')

def fix_my_code(error_message, source_code):

    prompt = f"""
    You are an expert software engineer. A Python script failed.
    ERROR: {error_message}
    ORIGINAL CODE:
    {source_code}
    
    TASK: Fix the code. 
    CONSTRAINTS: Return ONLY the raw code. No markdown code blocks (```), no explanations.
"""
    
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":

    # 1. read the broken file
    with open("app.py", "r") as f:
        broken_code = f.read()
    
    # 2. reads from the logs file to get the error message (now it is hardcoded)
    test_error = "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
    
    # 3. get the fix
    fixed_code = fix_my_code(test_error, broken_code)
    
    # 4. overwrite the file with the fix
    with open("app.py", "w") as f:
        f.write(fixed_code)