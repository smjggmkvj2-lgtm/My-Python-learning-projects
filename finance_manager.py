import sqlite3
from datetime import datetime 


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
    def add_transaction(self, transaction_type, description, amount, date, category):
        self.c.execute('INSERT INTO transactions (type, description, amount, date, category) VALUES (?, ?, ?, ?, ?)', (transaction_type, description, amount, date, category))
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
    def edit_transaction(self, transaction_id, transaction_type=None, description=None, amount=None, date=None, category=None):
        self.c.execute('SELECT * FROM transactions WHERE id = ?', (transaction_id,))
        transaction = self.c.fetchone()
        if transaction is None:
            print("Transaction not found")
            return
        if transaction_type is None:
            transaction_type = transaction[1]
        if description is None:
            description = transaction[2]
        if amount is None:
            amount = transaction[3]
        if date is None:
            date = transaction[4]
        if category is None:
            category = transaction[5]
        self.c.execute('UPDATE transactions SET type = ?, description = ?, amount = ?, date = ?, category = ? WHERE id = ?', (transaction_type, description, amount, date, category, transaction_id))
        self.conn.commit()
    def delete_transaction(self, transaction_id):
        self.c.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
        self.conn.commit()
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
    def monthly_stats(self, month, year):
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
    def get_transaction_by_id(self, transaction_id):
        self.c.execute('SELECT * FROM transactions WHERE id = ?', (transaction_id,))
        transaction = self.c.fetchone()
        return transaction

    def close(self):
        self.conn.close()


def main():
    manager = FinanceManager()

    while True:
        print("1 - Add Transaction")
        print("2 - Show Transactions")
        print("3 - Edit Transaction")
        print("4 - Delete Transaction")
        print("5 - Calculate Balance")
        print("6 - Monthly Stats")
        print("7 - Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                transaction_type = input("Enter transaction type (income/expense): ")
                if transaction_type in ("income", "expense"):
                    break
                print("Invalid type. Please enter 'income' or 'expense'.")
            description = input("Enter transaction description: ")
            while True:
                try:
                    amount = float(input("Enter transaction amount: "))

                    if amount <= 0:
                        print("Amount must be greater than 0.")
                        continue

                    break

                except ValueError:
                    print("Invalid amount. Please enter a number.")
            date = input("Enter transaction date (DD.MM.YYYY): ")
            while True:
                try:
                    datetime.strptime(date, "%d.%m.%Y")
                    break
                except ValueError:
                    print("Invalid date format. Please enter date in DD.MM.YYYY format.")
                    date = input("Enter transaction date (DD.MM.YYYY): ")
            category = input("Enter transaction category: ")
            manager.add_transaction(transaction_type, description, amount, date, category)
            print("Transaction added successfully.")
        elif choice == "2":
            manager.show_transactions()
        elif choice == "3":
            while True:
                try:
                    transaction_id = int(input("Enter transaction ID to edit: "))
                    break
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            transaction = manager.get_transaction_by_id(transaction_id)
            if transaction is None:
                print("Transaction not found")
                continue    
            while True:
                transaction_type = input("Enter new transaction type (income/expense) or leave blank to keep current: ")
                if transaction_type == "":
                    transaction_type = None
                    break
                if transaction_type in ("income", "expense"):
                    break
                print("Invalid type. Please enter 'income', 'expense' or leave blank.")
            description = input("Enter new transaction description or leave blank to keep current: ")
            if description == "":
                description = None
            while True:
                amount_input = input("Enter new transaction amount or leave blank to keep current: ")
                if amount_input == "":
                    amount = None
                    break
                try:
                    amount = float(amount_input)
                    if amount <= 0:
                        print("Amount must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            date = input("Enter new transaction date (DD.MM.YYYY) or leave blank to keep current: ")
            while True:
                if date == "":
                    date = None
                    break
                try:
                    datetime.strptime(date, "%d.%m.%Y")
                    break
                except ValueError:
                    print("Invalid date format. Please enter date in DD.MM.YYYY format or leave blank.")
                    date = input("Enter new transaction date (DD.MM.YYYY) or leave blank to keep current: ")
            category = input("Enter new transaction category or leave blank to keep current: ")
            if category == "":
                category = None
            manager.edit_transaction(transaction_id, transaction_type, description, amount, date, category)
            print("Transaction updated successfully.")
        elif choice == "4":
            while True:
                try:
                    transaction_id = int(input("Enter transaction ID to delete: "))
                    break
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            transaction = manager.get_transaction_by_id(transaction_id)
            if transaction is None:
                print("Transaction not found")
                continue
            manager.delete_transaction(transaction_id)
            print("Transaction deleted successfully.")
        elif choice == "5":
            manager.calculate_balance()
        elif choice == "6":
            month = input("Enter month (MM): ")
            year = input("Enter year (YYYY): ")
            if not month.isdigit() or not year.isdigit() or int(month) < 1 or int(month) > 12 or len(year) != 4:
                print("Invalid month or year format. Please enter month as MM and year as YYYY.")
                continue
            month = f"{int(month):02d}" 
            manager.monthly_stats(month, year)
        elif choice == "7":
            manager.close()
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()