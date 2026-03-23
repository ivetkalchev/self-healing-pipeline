def analyze_transactions(transactions):
    valid_amounts = []
    for t in transactions:
        val = t.get("amount")
        if val is not None:
            try:
                valid_amounts.append(float(val))
            except (ValueError, TypeError):
                continue
    
    if not valid_amounts:
        return {"sum": 0, "average": 0, "max": None, "min": None}
        
    total_val = sum(valid_amounts)
    return {
        "sum": total_val,
        "average": total_val / len(valid_amounts),
        "max": max(valid_amounts),
        "min": min(valid_amounts)
    }

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

if __name__ == "__main__":
    main()