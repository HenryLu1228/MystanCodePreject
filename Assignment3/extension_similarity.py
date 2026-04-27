"""
File: similarity.py (extension)
Name:呂沅翰
----------------------------
This program is an extension of Assignment 3.

It compares a short DNA sequence, s2, with all possible
subsequences of a longer DNA sequence, s1. The approach
used in this program is similar to the techniques commonly
applied in the bioinformatics industry.
"""


def main():
    s1 = input("Please give me a DNA sequence to search: ")
    s2 = input("What DNA sequence would you like to match? ")

    best_match = ""
    max_count = -1

    # 滑動視窗
    for i in range(len(s1) - len(s2) + 1):
        substring = s1[i:i + len(s2)]
        count = 0

        # 計算相同字母數
        for j in range(len(s2)):
            if substring[j] == s2[j]:
                count += 1

        # 更新最佳結果
        if count > max_count:
            max_count = count
            best_match = substring

    print("The best match is:", best_match)

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
