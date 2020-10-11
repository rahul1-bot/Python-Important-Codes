"""
------------------------------LIST DATA TYPE -----------------------------------------
Program Flow -
1) Main-Menu
2) Options: - a) insertion -> from start; from middle; from end
              b) deletion -> from start; from middle; from end
              c) Modifying -> from start; form middle; from end

3) Exit
--------------------------------------------------------------------------------------
"""
def MainMenu():
    ## Menu Structure
    print("-"*15 + "LIST MAIN MENU" + "-"*15)
    options = ["List Input", "Insertion", "Deletion", "Modification"]
    for index, value in enumerate(options):
        print("{}: {}".format(index+1, value))
    print("Enter '0' to Exit")

    ## valid choices
    valid_choice = [str(i) for i in range(1, len(options) + 1)]

    # options_functions = (ListInput(), Insertion())  #Deletion(), Modification()]
    ## User Inputs
    while True:
        choice = input("Please Enter your Choice {1-4} : ")
        if choice in valid_choice:
            index = int(choice) - 1
            print("You have Selected : {}".format(options[index]))
            # print("-"*15)
            # options_functions(index)
            # print("-"*15)
        elif choice == "0":
            print("Exiting from the Main-Menu....")
            break
        else:
            print("Please Enter options between {1-5} : ")


def Deletion(User_list):
    """
    Paras - a) Min_value = Minimium value for the list below this min values, all the elements will be removed.
            b) Max_values = Maximum values for the list above this, all the elements will be removed.

     - Returns the elements -V- set(input_list)
    """
    top_index = len(User_list) - 1
    print("-"*15+ "INPUTTED LIST"+ "-"*15)
    for index, value in enumerate(User_list):
        print("{}: {}".format(index+1, value))

    min_value, max_value = map(float, input("Enter the Min and Max Values : ").split(" "))

    print("Deleted elements != {} < values < {}".format(min_value, max_value))
    print("-"*15 + "AFTER DELETION" + "-"*15)
    for index, value in enumerate(reversed(User_list)):
        if (value < min_value) or (value > max_value):
            print("Deleted {} at index : {}".format(value, top_index - index))
            del User_list[top_index - index]

    print(User_list)

def main():
    MainMenu()
    Deletion(list(range(100, 401, 25)))
if __name__ == "__main__":
    main()

