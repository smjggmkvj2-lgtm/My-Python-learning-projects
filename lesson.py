class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}€. Balance: {self.balance}€")

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds!")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrawed {amount}€. Balance: {self.balance}€")
    def show_balance(self):
        print(f"Owner: {self.owner}")
        print(f"Current balance: {self.balance}€")
    def save_account(self):
        with open("Bank_Info.txt", "w") as file:
            file.write(f"{self.owner}\n")
            file.write(f"{self.balance}\n")
    def load_account(self):
        try:
            with open("Bank_info.txt", "r") as file:
                lines = file.readlines()
                self.owner = lines[0].strip()
                self.balance = float(lines[1].strip())
        except FileNotFoundError:
            pass
account = BankAccount("", 0)
account.load_account()
if account.owner == "":
    name = input("Enter your name: ")
    start_balance = float(input("Enter your star balance: "))
    account.owner = name
    account.balance = start_balance
while True:
    choice = input("1 - Deposit, 2 - Withdraw, 3 - Show balance, 4 - Exit: ")
    if choice == "1":
        try:
            to_deposit = float(input("How much do you want to deposit:"))
            account.deposit(to_deposit)
        except ValueError:
            print("You can use only numbers")
    elif choice == "2":
        try:
            to_withdraw = float(input("How much do you want to withdraw: "))
            account.withdraw(to_withdraw)
        except ValueError:
            print("You can use only numbers")
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        account.save_account()
        print("Bye, thanks for choosing us")
        break
    else:
        print("Wrong choice")