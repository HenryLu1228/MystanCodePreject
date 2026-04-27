"""
File: string_score.py
Name:呂沅翰
------------------------------
This program calculates a score for a given string based on
the types of characters it contains.

Digits are worth 1 point, uppercase letters are worth 2 points,
and lowercase letters are worth 3 points. The score() function
iterates through each character in the string, adds up the
corresponding points, and prints the final total score.
"""


def main():
    """
    TODO:
    """
    score('1aB4rC')    # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    total = 0

    for ch in string:
        if ch.isdigit():  # 數字
            total += 1
        elif ch.isupper():  # 大寫字母
            total += 2
        elif ch.islower():  # 小寫字母
            total += 3

    print(total)


if __name__ == '__main__':
    main()