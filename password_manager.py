import sqlite3
from cryptography.fernet import Fernet
class PasswordManager:
    def __init__(self):
        self.conn = sqlite3.connect('passwords.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY,
                website TEXT,
                username TEXT,
                password TEXT
            )
        ''')
        self.conn.commit()
        try:
            with open("key.key", "rb") as f:
                self.key = f.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            with open("key.key", "wb") as f:
                f.write(self.key)
        self.fernet = Fernet(self.key)
    def add_password(self, website, username, password):
        encrypted = self.fernet.encrypt(password.encode())
        self.c.execute('INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)', (website, username, encrypted))
        self.conn.commit()
    def get_passwords(self):
        self.c.execute('SELECT * FROM passwords')
        passwords = self.c.fetchall()
        if len(passwords) == 0:
            print("There are no passwords stored right now")
            return
        else:
            for password in passwords:
                decrypted = self.fernet.decrypt(password[3]).decode()
                print(f"Id: {password[0]} | Website: {password[1]} | Username: {password[2]} | Password: {decrypted}")

password_manager = PasswordManager()

while True:
    print("\nPassword Manager")
    print("1. Add Password")
    print("2. Show Passwords")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        website = input("Enter website: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        password_manager.add_password(website, username, password)
        print("Password added successfully!")
    elif choice == "2":
        password_manager.get_passwords()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")