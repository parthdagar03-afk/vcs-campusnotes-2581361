print("Parth Dagar URN:2581361")
def show_menu():
    print("\n===== FreshMart Grocery List Manager =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Clear List")
    print("5. Exit")

grocery_list = []

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter item to add: ").strip()
        if item:
            grocery_list.append(item)
            print(f"'{item}' added to your grocery list.")
        else:
            print("Item name cannot be empty!")

    elif choice == "2":
        item = input("Enter item to remove: ").strip()
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"'{item}' removed from your grocery list.")
        else:
            print("Item not found in the list.")

    elif choice == "3":
        if grocery_list:
            print("\nYour Grocery List:")
            for index, item in enumerate(grocery_list, start=1):
                print(f"{index}. {item}")
        else:
            print("Your grocery list is empty.")


    elif choice == "4":
        grocery_list.clear()
        print("All items have been cleared from your grocery list.")

    elif choice == "5":
        print("Thank you for using FreshMart Grocery List Manager!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
