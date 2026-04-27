"""
File: name_sq.py (extension)
Name: 呂沅翰
----------------------------
This program is an extension of Assignment 3.

It asks the user to enter a name and then prints a
square pattern based on the given name to the console.
"""


def main():
    name = input("Name: ")

    for i in range(len(name)):
        line = ""
        for j in range(len(name)):
            index = (i + j) % len(name)
            line += name[index]
        print(line)

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
