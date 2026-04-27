"""
File: count_ch.py
Name:
----------------------
The goal of this program is to count
the number of uppercase letters in
different words: 'ApPLE', 'Jerry', and 'PineApple'.

It defines a function called
num_upper() to perform the counting.
This function is then used to count
the uppercase letters in several
example words and print the results.
"""

def num_upper(s):
   ans = 0  # 將計數器初始化為 0
   for i in range(len(s)):
      # 檢查索引 i 處的字元是否為大寫
      if s[i].isupper():
         ans += 1
   return ans


def main():
    s = 'ApPLE'
    s2 = 'Jerry'
    s3 = 'PineApple'
    print(s + ' has ' + str(num_upper(s)) + ' uppercase letters.')
    print(s2 + ' has ' + str(num_upper(s2)) + ' uppercase letters.')
    print(s3 + ' has ' + str(num_upper(s3)) + ' uppercase letters.')


if __name__ == '__main__':
    main()