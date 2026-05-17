products = {}
def add_product():
    item = input("Enter an item you would like to add: ").strip().lower()
    if item == "":
        print("Item cannot be empty")
        return
    price_input = input("Enter price: ").strip()
    if not price_input.isdigit():
        print("Price must be number")
        return
    price = int((price_input))
    products[item] = price
def show_products():
    if len(products) == 0:
        print("List is empty")
    else:
        for item, price in products.items():
            print(item, "-", price)
def remove_product():
    if not products:
        print("List is empty")
    else:
        remove_item = input("Type in item you want to remove").strip().lower()
        if remove_item in products:
            item = (remove_item)
            del products[item]
        else:
            print("Item was not found")
def edit_price():
    if not products:
        print("List is empty")
        return
    price_edit = input("Enter item where you want to change the price: ").strip().lower()
    item = (price_edit)
    if item in products:
        price_input = input("Enter new price: ").strip()
        if not price_input.isdigit():
            print("Price must be a number")
            return
        new_price = int(price_input)
        products[item] = new_price
        print("Price updated!")
    else:
        print("Item was not found")
def total_price():
    if not products:
        print("List is empty")
    else:
        total = sum(products.values())
        print("Total price is" , total)
def search_item():
    if not products:
        print("List is empty")
        return
    item = input("Enter an item you want to find: ").strip().lower()
    if item in products:
        print("Found: ", item, "-", products[item])
    else:
        print("Item was not found")
def save_to_file():
    if not products:
        print("List is empty")
        return
    with open("products.txt" , "w") as file:
        for item, price in products.items():
            file.write(item + "-" + str(price) + "\n")
    print("Saved to file")
def load_from_file():
    with open("products.txt" , "r") as file:
        for line in file:
            line = line.strip()
            item, price=line.split("-")
            price = int(price)
            products[item]=price
    print("Loaded from file")
while True:
    choice = input("1 - Add product, 2 - Show products, 3 - Remove product, 4-Edit price,  5-Count total price, 6-Search item, 7-Save to file, 8-Load from file, 9 - Exit: ").strip()
    if choice == "":
        print("You need to choose something")
    elif choice == "1":
        add_product()
    elif choice == "2":
        show_products()
    elif choice == "3":
        remove_product()
    elif choice == "4":
        edit_price()
    elif choice == "5":
        total_price()
    elif choice == "6":
        search_item()
    elif choice == "7":
        save_to_file()
    elif choice == "8":
        load_from_file()
    elif choice == "9":
        print("Bye")
        break
    else:
        print ("Wrong choice")