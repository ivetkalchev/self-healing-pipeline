import sys
import json
import traceback
from processor import main

if __name__ == "__main__":
    
    try:
        result = main()
    
    except Exception as e:
        print("APPLICATION CRASHED")
        print(f"ERROR_TYPE: {type(e).__name__}")
        print(f"ERROR_MESSAGE: {str(e)}")

        with open("error.log", "w") as log:
            json.dump({
                "type": type(e).__name__,
                "message": str(e),
                "trace": traceback.format_exc()
            }, log)

        sys.exit(1)