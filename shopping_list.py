shopping_list = []
try:
    with open("shopping.txt" , "r") as file:
        lines = file.readlines()
        for line in lines:
            shopping_list.append(line.strip())
        print("Everything was loaded")
except FileNotFoundError:
    pass
def add_item():
    add = input("Enter an item you would like to add: ").strip().lower()
    if add == "":
        print("Item cannot be empty")
    elif add in shopping_list:
        print("Item alredy exists")
    else:
        shopping_list.append(add)
def show_list():
    if len(shopping_list) == 0:
        print("Shopping list is empty")
    else:
        print("Shopping list: ")
        for x in shopping_list:
            print(x)
        print("Total items: " , get_count())
def remove_item():
    if len(shopping_list) == 0:
        print("Shopping list is empty")
    else:
        print("Shopping list: ")
        for x in shopping_list:
            print(x)
        item = input("Enter an item you want to remove: ").strip().lower()
        if item in shopping_list:
            shopping_list.remove(item)
            print("Removed!")
        else:
            print("Item was not found")
def clear_list():
    if len(shopping_list) == 0:
        print("Shopping list is empty")
    else:
        shopping_list.clear()
        print("List was cleared!")
def get_count():
    return len(shopping_list)
def search_item():
    if len(shopping_list) == 0:
        print("Shopping list is empty")
    else:
        search = input("Enter an item you want to find: ").strip().lower()
        if search in shopping_list:
            print("Found")
        else:
            print("Not Found")
def save_to_file():
    if len(shopping_list) == 0:
        print("Shopping list is empty")
    else:
        with open("shopping.txt" , "w") as file:
            for x in shopping_list:
                file.write(x + "\n")
        print("file was saved")
while True:
    choice = input("1 - Add item, 2 - Show list, 3 - Remove item, 4 - Clear list, 5 - Search Item, 6 - Save to file, 7 - Exit  (print numbers only pls): ")
    if choice == "1":
        add_item()
    elif choice == "2":
        show_list()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        search_item()
    elif choice == "6":
        save_to_file()
    elif choice == "7":
        print("Byeee!!!((")
        break
    else:
        print("Wrong choice")