from MenuFunctions import new_user, add_habit, habit_tracker, view_users
from db import connect, create_table

# Connect to database and create the table if it doesn't exist
conn = connect()
create_table(conn)

def main():
    # Show Menu
    while True:
        print("-- Welcome to Habit Tracker --")
        print()

        print("Menu: ")
        print("1) Register New User")
        print("2) Add Habit (for existing user)")
        print("3) View Today's Habit")
        print("4) View All Users")
        print("5) Exit")

        print()
        
        try:
            menu_options = int(input("Enter a number 1-5: "))
        except ValueError:
            print("Please enter a number 1-5")
            print()
            continue

        match menu_options:
            case 1:
                new_user()
            case 2:
                add_habit()
            case 3: 
                habit_tracker()
            case 4:
                view_users()
            case 5:
                print("\nGoodbye!", end="")
                break
            case _: 
                print("Please enter a number 1-5")
                print()

# Start program if run directly
if __name__ == "__main__":
    main()