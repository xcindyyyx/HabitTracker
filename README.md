# Habit Tracker CLI
This is a command-line Habit Tracker using **Python** and **SQLite3**.

It lets you:
1. Register New User
2. Add Habit (for existing user)
3. View Today’s Habit
4. View All Users
5. Exit

When the program runs, it shows this menu:

— Welcome to Habit Tracker —

Menu:

1. Register New User
2. Add Habit (for existing user)
3. View Today’s Habit
4. View All Users
5. Exit

## Features Breakdown
### 1. Register New User
- Asks for first and last name
- Validates both inputs 
- Then gives a unique user ID like: 'Welcome John Doe! Your user ID is 1.'

### 2. Add Habit (for existing user)
- Asks for your user ID
- Asks what your habit is and how many times you'll do it today
- Saves it to the database

### 3. View Today’s Habit
- Asks for your user ID
- Shows your habits and how many times you plan to do them

### 4. View All Users
- Lists every user with their name and user ID
### 5. Exit
- Ends the program

## Tech Used
- Python
- SQLite3
- Git
- Notion (for planning & pseudocode)

## Example Pseudocode Snippet (from Notion)

If input is valid: 
Enter a number 1-5: INT

If input is invalid:
Please enter a number 1-5

Output if user presses 1:
Welcome to Habit Tracker

Please enter your first name and last name

First Name: STRING

If input is valid: continue
If input is invalid: Repromt the user to enter  first_name

Last Name: STRING

If input is valid: continue
If input is invalid: Repromt the user to enter last_name

SQL assigns user ID
Output: Welcome first_name last_name! Your user ID is 5.


## Warning
Inside 'db.py' file, you'll see two lines:
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("DROP TABLE IF EXISTS habits")

These will delete ALL data from your database.
Only uncomment if you want to completely reset users and habits table.
Once you uncomment and run the file, everything will be gone.

## How to Run
Python must be installed. Run program in a terminal:
python HabitTracker.py