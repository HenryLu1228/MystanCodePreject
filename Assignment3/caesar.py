"""
File: caesar.py
Name:呂沅翰
------------------------------
This program demonstrates the idea of the Caesar cipher.

The user is first asked to enter a number that determines
how much the alphabet should be shifted to form a cipher
table. After that, any input string will be encrypted
using the generated cipher.
"""



# 定義全局變數 ALPHABET
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def main():
    n = int(input('Secret number: '))
    new_alpha = create_new_alpha(n)

    # 印出字母表供對照（選配，可用於檢查）
    print('old alpha: ' + ALPHABET)
    print('new alpha: ' + new_alpha)

    ciphered = input("What is the ciphered string: ")

    # 呼叫解密函式
    ans = decipher(ciphered, new_alpha)

    print("The deciphered string is:", ans)


def create_new_alpha(n):
    """
    根據偏移量 n 建立新的字母表。
    使用切片法：將最後面 n 個字母搬到最前面。
    """
    ans = ''
    ans += ALPHABET[26 - n:]  # 取出後段的字母 (例如 WXYZ)
    ans += ALPHABET[:26 - n]  # 取出前段的字母 (例如 A...V)
    return ans


def decipher(ciphered, new_alpha):
    """
    解密邏輯：
    將 ciphered 中的字元對應新舊字母表來還原。
    """
    result = ""
    for char in ciphered:
        upper_char = char.upper()  # 處理 Case-insensitive

        # 如果該字元是英文字母
        if upper_char in new_alpha:
            # 1. 找到在 new_alpha 中的索引位置
            index = new_alpha.find(upper_char)
            # 2. 從原始 ALPHABET 中取出對應位置的字母
            result += ALPHABET[index]
        else:
            # 如果不是字母（如空格或驚嘆號），保持原樣
            result += char

    return result


if __name__ == "__main__":
    main()