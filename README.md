Budget Tracker

Description:
Budget Tracker is a command-line application built in Python for my CS50P final project. It allows a user to log income and expenses, organize spending into categories, check their current balance, and view a breakdown of how much they've spent in each category — with all data automatically saved between sessions using a CSV file.

The motivation behind this project was to build something genuinely useful rather than purely academic. Everyone deals with tracking money in some form, and a simple, no-frills CLI tool felt like a good way to apply the concepts covered throughout CS50P — functions, loops, dictionaries, file I/O, exception handling, and testing — to a real, practical problem.

How it works
When the program runs, it presents a simple numbered menu with five options: add income, add an expense, view balance, view a category breakdown, and exit. Each transaction, whether income or an expense, is represented internally as a dictionary with three keys: amount, type (either "income" or "expense"), and category (e.g. "food", "rent", "transport", or "income" for income entries). Storing transactions this way, rather than as separate parallel lists, made it easier to write clean, reusable logic for calculating totals and breakdowns.

All transactions are stored in memory in a list for the duration of the program, and written out to transactions.csv when the user exits. On startup, the program reads this file back in, so a user's data persists across multiple runs without needing a database.
