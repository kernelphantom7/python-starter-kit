"""
classes_and_objects.py
-----------------------
Intro to object-oriented programming (OOP) in Python.
"""

class Player:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def level_up(self):
        self.level += 1
        print(f"{self.username} leveled up! New level: {self.level}")

    def display_info(self):
        print(f"Player: {self.username} | Level: {self.level}")

# Creating an object
player1 = Player("kernelphantom7", 1)

player1.display_info()
player1.level_up()
player1.display_info()
