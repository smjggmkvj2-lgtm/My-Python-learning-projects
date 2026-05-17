class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
class ContactManager:
    def __init__(self):
        self.contacts = []
    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
    def show_contacts(self):
        if len(self.contacts) == 0:
            print("There is no contacts on the list")
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name} Phone: {contact.phone} Email: {contact.email}")
    def find_contact(self, name):
        if len(self.contacts) == 0:
            print("There is no contacts on the list")
            return
        for contact in self.contacts:
            if contact.name == name:
                print(f"Found Phone: {contact.phone} Email: {contact.email}")
                return
        print("Contact was not found")
    def remove_contact(self, name):
        if len(self.contacts) == 0:
            print("No contacts found")
            return
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {contact.name}, was removed")
                return
        print("Contact was not found")
    def save_to_file(self):
        with open("Contacts.txt" , "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name}\n")
                file.write(f"{contact.phone}\n")
                file.write(f"{contact.email}\n")
                file.write(f"---\n")
    def load_from_file(self):
        try:
            with open("contacts.txt" , "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    name = lines[i].strip()
                    phone = lines[i+1].strip()
                    email = lines[i+2].strip()
                    i += 4
                    self.add_contact(name, phone, email)
        except FileNotFoundError:
            pass
manager = ContactManager()
manager.load_from_file()

while True:
    choice = input("1 - Add, 2 - Show, 3 - Find, 4 - Remove, 5 - Exit: ")
    if choice == "1":
        name = input("Enter the name").lower().strip()
        phone = input("Enter the phone number")
        if not phone.lstrip("+").isdigit():
            print("Phone can be only numbers")
            continue
        email = input("Enter an email").strip()
        manager.add_contact(name, phone, email)
    elif choice == "2":
        manager.show_contacts()
    elif choice == "3":
        name = input("Enter the contact you want to find: ").lower().strip()
        manager.find_contact(name)
    elif choice == "4":
        name = input ("Enter an contact you want to remove: ").lower().strip()
        manager.remove_contact(name)
    elif choice == "5":
        print("Bye")
        manager.save_to_file()
        break
    else:
        print("Wrong choice")