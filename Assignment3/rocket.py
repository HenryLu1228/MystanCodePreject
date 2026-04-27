"""
File: rocket.py
Name:呂沅翰
-----------------------
This program implements a console-based application that
draws an ASCII art rocket.

The size of the rocket is determined by a constant named
SIZE, which is defined at the top of the file. The output
format should match the sample run shown in the Assignment 3 handout.
"""

# This constant determines rocket size.
SIZE = 3


"""
File: rocket.py
Name: 
-----------------------
This program prints a rocket ship of varying sizes 
based on the constant SIZE.
"""

# Constant to control the scale of the rocket
SIZE = 3


def main():
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    # Outer loop for each row
    for i in range(SIZE):
        # Print leading spaces
        for j in range(SIZE - i):
            print(" ", end="")
        # Print left slashes
        for k in range(i + 1):
            print("/", end="")
        # Print right slashes
        for l in range(i + 1):
            print("\\", end="")
        print("") # Move to next line


def belt():
    print("+", end="")
    for i in range(SIZE * 2):
        print("=", end="")
    print("+")


def upper():
    for i in range(SIZE):
        print("|", end="")
        # Dots on the left
        for j in range(SIZE - i - 1):
            print(".", end="")
        # Slanted section left
        for k in range(i + 1):
            print("/", end="")
        # Slanted section right
        for l in range(i + 1):
            print("\\", end="")
        # Dots on the right
        for m in range(SIZE - i - 1):
            print(".", end="")
        print("|")


def lower():
    for i in range(SIZE):
        print("|", end="")
        # Dots on the left
        for j in range(i):
            print(".", end="")
        # Slanted section left
        for k in range(SIZE - i):
            print("\\", end="")
        # Slanted section right
        for l in range(SIZE - i):
            print("/", end="")
        # Dots on the right
        for m in range(i):
            print(".", end="")
        print("|")


# Standard boilerplate for running the program


if __name__ == '__main__':
    main()
