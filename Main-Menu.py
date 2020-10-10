def MainMenu():
    print("-"*15 + "MAIN-MENU" + "-"*15)
    options = ["Computer", "Monitor", "DVD", "Keyboard", "Mouse", "Mouse Pad", "Laptop", "Phone"]
    for i, value in enumerate(options):
        print("{}: {}".format(i+1, value))
    print("Enter '0' to Exit")

    selected_options = []
    valid_choices = [str(i) for i in range(1, len(options) +1)]

    while True:
        choice = str(input("Enter your choice from the list : "))
        if choice in valid_choices:
            index = int(choice) - 1
            print("{} added in Cart".format(options[index]))
            selected_options.append(options[index])
        elif choice == "0":
            print("Exiting from the Main-Menu")
            break
        else:
            print("Please enter the choice [0-5]")

    print("-"*15 + "Selected Items" + "-"*15)
    for i, value in enumerate(selected_options):
        print("{}: {}".format(i+1, value))


def main():
    MainMenu()
if __name__ == "__main__":
    main()

