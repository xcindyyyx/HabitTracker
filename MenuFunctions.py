import sqlite3
from db import connect, create_table

def new_user():
    print("Welcome to Habit Tracker")
    print()
    print("Please enter your first name and last name")

    # Once we have input connect to db
    conn = connect()
    cursor = conn.cursor()

    while True:
        try:
            first_name = input("First Name: ").strip()
            # If output is True capitalize first letter
            if first_name.isalpha():
                first_name = first_name.capitalize()
                break                            # Exit the loop
            else:
                raise ValueError                 # This triggers except    

        except ValueError:
            print("Please enter only letters and spaces. No numbers or symbols.")
            print()
            continue                             # Ask user to enter the first name again    

    while True:
        try:
            last_name = input("Last Name: ").strip()
            # If output is True capitalize first letter
            if last_name.isalpha():
                last_name = last_name.capitalize()
                break                            # Exit the loop
            else:
                raise ValueError                 # This triggers except    

        except ValueError:
            print("Please enter only letters and spaces. No numbers or symbols.")
            print()
            continue                             # Ask user to enter the last name again    

    cursor.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
    user_id = cursor.lastrowid # Get the user_id that was created
    
    conn.commit()
    conn.close()

    print(f"Welcome {first_name} {last_name}! Your user ID is {user_id}")
    print()
    return user_id  # Allows user_id to be used in other parts of the program

def add_habit():
    print('You picked "Add Habit"\n')

    conn = connect()
    cursor = conn.cursor()

    user_id = input("User ID: ")

    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    if user is None:
        print("User ID does not exist\n")
        return                  # Exit the function
    else: 
        # Welcome the user
        first_name = user[1]    # Gets the 2nd item from the tuple
        last_name = user[2]     # Gets the 3rd item from the tuple
        print(f"Welcome, {first_name} {last_name}!\n")
    
    while True:
        try:
            habit_name = input("Enter the habit: ").strip()
            # Remove space and check if only letters are left
            if habit_name.replace(" ", "").isalpha():
                break                            # Exit the loop
            else:
                raise ValueError                 # This triggers except    

        except ValueError:
            print("Please enter only letters and spaces. No numbers or symbols.")
            print()
            continue                             # Ask user to enter the habit again

    while True:
        try:
            habit_number = int(input("Number of times this habit will be done: "))
            break                               # Exit the loop
        except ValueError:
            print("Please enter a number")
            print()
            continue                            # Ask the user the number of times the habit will be done again

    cursor.execute("INSERT INTO habits (habit_name, habit_number, user_id) VALUES (?, ?, ?)", (habit_name, habit_number, user_id,))
    conn.commit()
    conn.close()

    print()
    print(f"Your habit for today is: {habit_name}. You'll do it {habit_number} times today.")
    print()
    return habit_name, habit_number
    
def habit_tracker():
    print('You picked "View Today\'s Habit"')
    print()

    conn = connect()
    cursor = conn.cursor()

    user_id = input("User ID: ")
    
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    if user is None:
        print("User ID does not exist\n")
        return                  # Exit the function
    else: 
        # Welcome the user
        first_name = user[1]    # Gets the 2nd item from the tuple
        last_name = user[2]     # Gets the 3rd item from the tuple
        print(f"Welcome, {first_name} {last_name}!\n")
    
    # Get all habits that the user has
    cursor.execute("SELECT habit_name, habit_number FROM habits WHERE user_id = ?", (user_id,))
    habits = cursor.fetchall()

    if not habits:
        print("No habits were found for that user.")
    else:
        for habit in habits:
            print(f"Habit: {habit[0]}")
            print(f"Number of times: {habit[1]}") 
            print()  

def view_users():
    conn = connect()
    cursor = conn.cursor()

    # Get all users
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    if rows:
        print("\nAll Users ")
        print("----------")
        for row in rows:
            print(row)
            print()
    else: 
        print("No users found\n")

    conn.close()

