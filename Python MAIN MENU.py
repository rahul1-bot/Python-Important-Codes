def Main_Menu():
    print("-"*15 + "MAIN MENU" + "-"*15)
    options = ["Computer", "Monitor", "DVD", "Keyboard", "Mouse", "Mouse Pad", "Laptop", "Phone"]
    for i, value in enumerate(options):
        print("{}: {}".format(i+1, value))
    print("Enter '0' to Exit")


    selected_items = []
    valid_options = [str(i) for i in range(1, len(options)+1)]


    while True:
        choice = str(input("Please Enter the choice from the list : "))
        if choice in valid_options:
            index = int(choice) - 1
            if options[index] in selected_items:
                print("{} already added in Cart".format(options[index]))
            else:
                print("{} added in the Cart".format(options[index]))
                selected_items.append(options[index])
        elif choice == "0":
            print("Exiting from the Main Menu")
            break
        else:
            print("Please Enter the choice: [1-5]")


    selected_items.sort()
    print("-"*15 + "Selected Items" + "-"*15)
    for i, value in enumerate(selected_items):
        print("{}: {}".format(i+1, value))


def main():
    Main_Menu()
if __name__ == "__main__":
    main()