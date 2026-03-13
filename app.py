import sys

def process_data(data_list):
    total = 0
    for item in data_list:
        total += item 
    
    return total

if __name__ == "__main__":
    my_data = [5, 15, "10", 20]
    
    try:
        result = process_data(my_data)
        print(f"✅ Success! The total is: {result}")
    except Exception as e:
        print(f"❌ APPLICATION CRASHED")
        print(f"ERROR_TYPE: {type(e).__name__}")
        print(f"ERROR_MESSAGE: {e}")
        sys.exit(1)