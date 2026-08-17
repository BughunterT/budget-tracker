import csv
import os

running = True

def main():
    global running
    while running:
        print("1-income\n" \
        "2-expense\n" \
        "3-balance\n" \
        "4-breakdown\n" \
        "5-exit")
        choice = input("enter a number corresponding to what you want: ").strip()

        if choice == "1":
            into()
            
        elif choice == "2":
            out()
            
        elif choice == "3":
            print(f"you have £{balance(transactions)} pounds")

        elif choice == "4":
            for category, total in breakdown(transactions).items():
                print(f"{category}: £{total}")

        elif choice == "5":
            save_transactions()
            running = False

        else:
            print("invalid input")

def load_transactions():
    try:
        with open("transactions.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            loaded = []
            for row in reader:
                row["amount"] = float(row["amount"])
                loaded.append(row)
            return loaded
        
    except FileNotFoundError:
        return []

def into():
    type_ = "income"
    amount = float(input("what is the amount: "))
    into_dict = {"amount": amount,
                 "type": type_,
                 "category": type_}
    
    transactions.append(into_dict)

def out():
    type_ = "expense"
    amount = float(input("what is the amount: "))
    category = input("what category (food, rent, transport, utilities): ")
    expense_dict = {"amount": amount,
                 "type": type_,
                 "category" : category}
    
    transactions.append(expense_dict)

def breakdown(transactions):
    categories = {}
    for transaction in transactions:
        if transaction["type"] == "expense":
            if transaction["category"] in categories:
                categories[transaction["category"]] += transaction["amount"]
            else:
                categories[transaction["category"]] = transaction["amount"]

    return categories



def balance(transactions):
    total = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            total += transaction["amount"]
            
        elif transaction["type"] == "expense":
            total -= transaction["amount"]

    return total

def save_transactions():
    with open("transactions.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "type", "category"])
        writer.writeheader()
        for transaction in transactions:
            writer.writerow(transaction)


transactions = load_transactions()
if __name__ == "__main__":
    main()