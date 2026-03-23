def analyze_transactions(transactions):
    summary = {
        "total": 0,
        "average": 0,
        "max": None,
        "min": None
    }
    
    for t in transactions:
        summary["total"] += t["amount"]
        
        if t["amount"] > summary["max"]:
            summary["max"] = t["amount"]
        
        if t["amount"] < summary["min"]:
            summary["min"] = t["amount"]
    
    summary["average"] = summary["total"] / len(transactions)
    
    return summary

def load_transactions():
    return [
        {"amount": 100},
        {"amount": "250"}, 
        {"value": 300},     
        {"amount": -50},
        {"amount": None}     
    ]

def main():
    transactions = load_transactions()
    
    result = analyze_transactions(transactions)
    
    print("Total:", result["sum"])
    print("Average:", result["average"])
    print("Max:", result["max"])
    print("Min:", result["min"])