import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-3-flash-preview')

def fix_my_code(error_message, source_code):
    print("🤖 Gemini is analyzing the crash...")
    
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
    # 1. Read the broken file
    with open("app.py", "r") as f:
        broken_code = f.read()
    
    # 2. Hardcode a test error for now (later this will come from logs)
    test_error = "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
    
    # 3. Get the fix
    fixed_code = fix_my_code(test_error, broken_code)
    
    # 4. Overwrite the file with the fix
    with open("app.py", "w") as f:
        f.write(fixed_code)
        
    print("✅ File app.py has been updated by the AI Agent!")