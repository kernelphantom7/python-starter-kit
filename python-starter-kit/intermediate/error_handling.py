"""
error_handling.py
------------------
Basic try/except examples for handling errors.
"""

def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except TypeError:
        print("Error: Both values must be numbers.")
    finally:
        print("Operation complete.\n")

divide(10, 2)
divide(5, 0)
divide("a", 3)
