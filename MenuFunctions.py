import sqlite3
from db import connect


# DO NOT FORGET TO PROMPT THE USER FOR QUESTIONS this is a CLI program remember.
def new_user():
    print("Welcome to Habit Tracker")
    print()
    print("Please enter your first name and last name")

    first_name = input("First Name: ")       
    last_name = input("Last Name: ")   

    # Once we have input connect to db
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)")
    user_id = cursor.lastrowid # Get the user_id that was created
    
    conn.commit()
    conn.close()

    print(f"Welcome {first_name} {last_name}! Your user ID is {user_id}")
    return user_id  # Allows user_id to be used in other parts of the program

def add_habit():

    print('You picked "Add Habit"\n')
    
    while True:
        try:
            habit = input("Enter the habit: ")

            # Remove space and check if only letters are left
            if habit.replace(" ", "").isalpha():
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

    print()
    print(f"Your habit for today {habit} and it'll be done {habit_number} times")
    print()
    return habit, habit_number
    
def habit_tracker():
    # print('You picked "View Today\'s Habit"')
    # print()
    # print("Progress Menu")
    # print("1. View Name of Habit")
    # print("2. View Current Progress")

    # while True:
    #     try:
    #         progress_menu = int(input("Enter a number 1-2: "))                          
    #     except ValueError:
    #         print("Please enter a number")
    #         print()
    #     else:
    #         match progress_menu:
    #             case 1: 
    #                 add_habit(habit)
    #             case 2:
    #                 i=0
    #                 for i in habit_number:
    #                     print(habit_number)
    #             case _:
    #                 print("Please enter a number")


    # return progress_menu      
    pass   

    def view_users():
        pass


    # You will write all the habits necessities here

