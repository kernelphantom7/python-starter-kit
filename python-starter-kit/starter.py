"""
starter.py
-----------
Main entry script for the Python Starter Kit.

This file acts as a central launch point for testing code,
importing modules from different folders, and experimenting
with Python concepts as you learn.

Feel free to modify, break things, fix them, and explore.
"""

from basics.functions import greet
from basics.variables import name
from intermediate.classes_and_objects import Player

def main():
    print("\n=== PYTHON STARTER KIT ===\n")

    # Test a basic function
    print(greet("Jeremie"))

    # Show a variable imported from another file
    print(f"Imported name from basics/variables.py: {name}")

    # Create and use a class from intermediate/
    player = Player("kernelphantom7", 1)
    player.display_info()
    player.level_up()

    print("\nStarter script executed successfully.\n")

if __name__ == "__main__":
    main()
