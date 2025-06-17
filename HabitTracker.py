# This will be our main file

def main():
    # Show Menu
    while True:
        print("-- Welcome to Habit Tracker --")
        print()

        print("Menu: ")
        print("1) Add Habit")
        print("2) View Today's Habit")
        print("3) Exit")

        print()
        
        try:
            menu_options = int(input("Enter a number 1-3: "))
        except ValueError:
            print("Please enter a number 1-3")
            print()
            continue

        match menu_options:
            case 1:
                add_habit()
            case 2:
                habit_tracker()
            case 3:
                print("\nGoodbye!", end="")
                break
            case _: 
                print("Please enter a number 1-3")
                print()

   
    # Loop Menu Options

    # Call MenuFunctions 



# Do __name___ = "__main__" and call main() function (So program will be ran through this file)
if __name__ == "__main__":
    main()