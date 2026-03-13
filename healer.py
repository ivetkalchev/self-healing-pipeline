import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-3-flash-preview')

def fix_my_code(error_log, source_code):
    prompt = f"""
    A Python script failed. Here is the log:
    {error_log}

    Here is the source code:
    {source_code}

    TASK: Fix the code so it doesn't crash. 
    Return ONLY the raw code. No markdown, no triple backticks.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    # 1. read the error log created by the pipeline
    if os.path.exists("error.log"):
        with open("error.log", "r") as f:
            actual_error = f.read()
    else:
        actual_error = "No error log found."

    # 2. read the source code
    with open("app.py", "r") as f:
        source = f.read()

    # 3. get the fix from Gemini
    fixed_code = fix_my_code(actual_error, source)

    # 4. save the fix
    with open("app.py", "w") as f:
        f.write(fixed_code)
    
    print("🤖 Agent successfully processed the real error logs.")