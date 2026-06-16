"""
input_validation.py
--------------------
Reusable input validation functions.
"""

def get_int(prompt):
    """Safely gets an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_float(prompt):
    """Safely gets a float from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")

def get_choice(prompt, options):
    """
    Gets a valid choice from a list of allowed options.
    Example:
        get_choice("Choose (a/b/c): ", ["a", "b", "c"])
    """
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        print(f"Invalid choice. Options: {', '.join(options)}")
