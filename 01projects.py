import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# Ensure the file exists with headers
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])

# Add new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave empty for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., food, transport, shopping): ")
    description = input("Enter description: ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!\n")

# Display all expenses
def view_expenses():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
        print(f"\n{'Date':<12} | {'Amount':<10} | {'Category':<15} | Description")
        print("-" * 60)
        for row in data[1:]:
            print(f"{row[0]:<12} | ₹{row[1]:<9} | {row[2]:<15} | {row[3]}")
        print()

# Delete expense by date or description
def delete_expense():
    keyword = input("Enter date or keyword to delete: ")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    new_data = [data[0]]
    deleted = False

    for row in data[1:]:
        if keyword in row[0] or keyword in row[3]:
            deleted = True
            continue
        new_data.append(row)

    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_data)

    if deleted:
        print("Expense(s) deleted successfully.\n")
    else:
        print("No matching expense found.\n")

# Filter by category
def filter_by_category():
    category = input("Enter category to filter: ")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    print(f"\nExpenses under category: {category}")
    print(f"{'Date':<12} | {'Amount':<10} | Description")
    print("-" * 50)
    for row in data[1:]:
        if row[2].lower() == category.lower():
            print(f"{row[0]:<12} | ₹{row[1]:<9} | {row[3]}")
    print()

# Get total spent by month
def monthly_summary():
    summary = {}
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    for row in data[1:]:
        date = row[0]
        amount = float(row[1])
        month = date[:7]
        summary[month] = summary.get(month, 0) + amount

    print("\nMonthly Expense Summary:")
    print("-" * 30)
    for month, total in summary.items():
        print(f"{month}: ₹{total:.2f}")
    print()

# Get total spent today
def today_summary():
    today = datetime.today().strftime('%Y-%m-%d')
    total = 0
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in list(reader)[1:]:
            if row[0] == today:
                total += float(row[1])
    print(f"\nTotal spent today ({today}): ₹{total:.2f}\n")

# Display help
def help_menu():
    print("""
Available Commands:
1. Add Expense          → Add a new expense entry
2. View Expenses        → List all expenses
3. Delete Expense       → Delete expense by date or keyword
4. Filter by Category   → Show expenses by category
5. Monthly Summary      → View total expense per month
6. Today Summary        → Show total expense for today
7. Help                 → Show this menu again
8. Exit                 → Quit the program
""")

# Main program
def main():
    initialize_file()
    help_menu()

    while True:
        choice = input("Enter your choice (1–8): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            filter_by_category()
        elif choice == '5':
            monthly_summary()
        elif choice == '6':
            today_summary()
        elif choice == '7':
            help_menu()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
