"""
file_handling.py
----------------
Reading from and writing to files in Python.
"""

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello! This file was created using Python.\n")
    file.write("File handling is easy once you learn the basics.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)
