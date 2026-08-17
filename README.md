______           _            _     _____              _
| ___ \         | |          | |   |_   _|            | |
| |_/ /_   _  __| | __ _  ___| |_    | |_ __ __ _  ___| | _____ _ __
| ___ \ | | |/ _` |/ _` |/ _ \ __|   | | '__/ _` |/ __| |/ / _ \ '__|
| |_/ / |_| | (_| | (_| |  __/ |_    | | | | (_| | (__|   <  __/ |
\____/ \__,_|\__,_|\__, |\___|\__|   \_/_|  \__,_|\___|_|\_\___|_|
                    __/ |
                   |___/
Description:
Budget Tracker is a command-line application built in Python for my CS50P final project. It allows a user to log income and expenses, organize spending into categories, check their current balance, and view a breakdown of how much they've spent in each category — with all data automatically saved between sessions using a CSV file.

The motivation behind this project was to build something genuinely useful rather than purely academic. Everyone deals with tracking money in some form, and a simple, no-frills CLI tool felt like a good way to apply the concepts covered throughout CS50P — functions, loops, dictionaries, file I/O, exception handling, and testing — to a real, practical problem.

How it works
When the program runs, it presents a simple numbered menu with five options: add income, add an expense, view balance, view a category breakdown, and exit. Each transaction, whether income or an expense, is represented internally as a dictionary with three keys: amount, type (either "income" or "expense"), and category (e.g. "food", "rent", "transport", or "income" for income entries). Storing transactions this way, rather than as separate parallel lists, made it easier to write clean, reusable logic for calculating totals and breakdowns.

All transactions are stored in memory in a list for the duration of the program, and written out to transactions.csv when the user exits. On startup, the program reads this file back in, so a user's data persists across multiple runs without needing a database.

Design decisions
One of the more important decisions I made partway through building this project was separating calculation logic from user interaction. Early versions of functions like balance() and breakdown() read directly from a global list and printed their results immediately, which made them impossible to test in isolation. I refactored both functions to accept a list of transactions as a parameter and return their result instead of printing it, moving the actual print() calls into main(). This is also why I split the expense-creation logic in out() into a separate make_expense() function — so it could take plain arguments and return a dictionary without depending on input(). This separation of concerns is what allowed me to write proper unit tests for the project's core logic in test_project.py.
