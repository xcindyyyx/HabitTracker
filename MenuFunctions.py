# DO NOT FORGET TO PROMPT THE USER FOR QUESTIONS this is a CLI program remember.


def add_habit():

    print('You picked "Add Habit"\n')

    try:
        habit = input("Enter the habit: ")
        habit_number = int(input("Number of times this habit will be done: "))
    except ValueError:
        print("Please enter a number 1-3")
        print()

    print()
    print(f"Your habit for today {habit} and it'll be done {habit_number} times")
    print()
    return habit, habit_number
    
def habit_tracker():
    pass
    # You will write all the habits necessities here

