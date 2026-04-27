"""
File: quadratic_solver.py
Name:呂沅翰
-----------------------
This program implements a console-based solver for a
quadratic equation.

It asks the user to input three values a, b, and c,
and computes the roots of the equation:
ax^2 + bx + c = 0.

The output format should match the sample run shown
in the Assignment 2 handout.
"""

import math


def main():
    """
    This file can calculate the quadratic: ax^2 + bx + c = 0
    And the a, b, c can input by the user
    """
    print('stanCode Quadratic Solver!')
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))
    # Calculate the discriminant value
    discriminant = (b*b) - (4*a*c)
    # Because a is the denominator, so a can't be zero
    if a == 0:
        print("The denominator can't be zero!")
    # There are two roots
    elif discriminant > 0:
        x1 = (-b+math.sqrt(discriminant))/(2*a)
        x2 = (-b-math.sqrt(discriminant))/(2*a)
        print('Two roots: ' + str(x1) + ' , ' + str(x2))
    # there is one root
    elif discriminant == 0:
        x = (-b/(2*a))
        print('One root: ' + str(x))
    # if discriminant < 0, there are no real roots
    else:
        print('No real roots')




# DO NOT EDIT CODE BELOW THIS LINE #



if __name__ == "__main__":
	main()
