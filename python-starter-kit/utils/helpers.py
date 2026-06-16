"""
helpers.py
-----------
General helper functions that can be reused across projects.
"""

def clear_line():
    """Prints a visual separator line."""
    print("-" * 40)

def title(text):
    """Prints a formatted title block."""
    clear_line()
    print(text.upper())
    clear_line()

def pause():
    """Waits for the user to press Enter."""
    input("\nPress Enter to continue...")
