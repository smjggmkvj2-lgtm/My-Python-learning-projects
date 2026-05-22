import sqlite3
class FinanceManager:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                type TEXT,
                description TEXT,
                amount REAL,
                date TEXT,
                category TEXT
            )
        ''')
        self.conn.commit()
    def add_transaction(self, type, description, amount, date, category):
        self.c.execute('INSERT INTO transactions (type, description, amount, date, category) VALUES (?, ?, ?, ?, ?)', (type, description, amount, date, category))
        self.conn.commit()
    def show_transactions(self):
        self.c.execute('SELECT * FROM transactions')
        transactions = self.c.fetchall()
        if len(transactions) == 0:
            print("There are no transactions recorded right now")
            return
        else:
            for transaction in transactions:
                print(f"Id: {transaction[0]} | Type: {transaction[1]} | Description: {transaction[2]} | Amount: {transaction[3]} | Date: {transaction[4]} | Category: {transaction[5]}")
    def calculate_balance(self):
        self.c.execute('SELECT * FROM transactions')
        transactions = self.c.fetchall()
        balance = 0
        for transaction in transactions:
            if transaction[1] == "income":
                balance += transaction[3]
            elif transaction[1] == "expense":
                balance -= transaction[3]
        print(f"Current Balance: {balance}")
    def monthly_stats(self):
            month = input("Enter month (MM): ")
            year = input("Enter year (YYYY): ")
            self.c.execute("SELECT * FROM transactions WHERE date LIKE ?", (f"%.{month}.{year}",))
            transactions = self.c.fetchall()
            if len(transactions) == 0:
                print("There are no transactions recorded for this month")
                return
            else:
                income = 0
                expense = 0
                for transaction in transactions:
                    if transaction[1] == "income":
                        income += transaction[3]
                    elif transaction[1] == "expense":
                        expense += transaction[3]
                print(f"Total Income: {income}")
                print(f"Total Expense: {expense}")
                print(f"Net Balance: {income - expense}")
            categories = {}
            for transaction in transactions:
                if transaction[1] == "expense":
                    category = transaction[5]
                    if category in categories:
                        categories[category] += transaction[3]
                    else:
                        categories[category] = transaction[3]
            if categories:
                top_category = max(categories, key=categories.get)
                print(f"Top Expense Category: {top_category} with amount {categories[top_category]}")
manager = FinanceManager()

while True:
    print("1 - Add Transaction")
    print("2 - Show Transactions")
    print("3 - Calculate Balance")
    print("4 - Monthly Stats")
    print("5 - Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        type = input("Enter transaction type (income/expense): ")
        while type != "income" and type != "expense":
            print("Invalid type. Please enter 'income' or 'expense'.")
            type = input("Enter transaction type (income/expense): ")
        description = input("Enter transaction description: ")
        amount = float(input("Enter transaction amount: "))
        date = input("Enter transaction date: ")
        category = input("Enter transaction category: ")
        manager.add_transaction(type, description, amount, date, category)
    elif choice == "2":
        manager.show_transactions()
    elif choice == "3":
        manager.calculate_balance()
    elif choice == "4":
        manager.monthly_stats()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")