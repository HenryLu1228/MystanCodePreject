"""
File: complement.py
Name:呂沅翰
----------------------------
This program uses string manipulation to solve a real-world
problem: finding the complementary strand of a DNA sequence.

The program provides different DNA sequences as Python strings.
These strings are case-sensitive, and your task is to generate
and output the correct complementary strand for each sequence.
"""


def main():
    """
    TODO:
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    # 特殊情況：空字串
    if dna == "":
        return "DNA strand is missing."

    result = ""

    for ch in dna:
        if ch == 'A':
            result += 'T'
        elif ch == 'T':
            result += 'A'
        elif ch == 'C':
            result += 'G'
        elif ch == 'G':
            result += 'C'

    return result

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
