# DO NOT FORGET TO PROMPT THE USER FOR QUESTIONS this is a CLI program remember.


# RERUN THIS FUNCTION AND FIX THE TRY/EXCEPT!
def add_habit():

    print('You picked "Add Habit"\n')
    
    while True:
        try:
            habit = input("Enter the habit: ")

            # Remove space and check if only letters are left
            if habit.replace(" ", "").isalpha():
                break       
            else:
                raise ValueError                 # This triggers except    

        except ValueError:
            print("Please enter only letters and spaces. No numbers or symbols.")
            print()
            return                               # Exit the function

    # try:
    #     habit_number = int(input("Number of times this habit will be done: "))
    #  except ValueError:
    #     print("Please enter a number")
    #     print()
    #     return                              # Exit the function

    # print()
    # print(f"Your habit for today {habit} and it'll be done {habit_number} times")
    # print()
    return habit, habit_number
    
def habit_tracker():
    pass
    # You will write all the habits necessities here

