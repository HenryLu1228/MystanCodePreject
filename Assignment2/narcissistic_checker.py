"""
File: extension4_narcissistic_checker.py
Name:呂沅翰
------------------------
This program repeatedly asks the user to enter a number and checks
whether the number is a narcissistic number.

A positive integer is called a narcissistic number if it is equal to
the sum of its own digits, where each digit is raised to the power of
the total number of digits.

For example, 153 is a narcissistic number because
1^3 + 5^3 + 3^3 = 153. By this definition, all single-digit numbers
are also considered narcissistic.

The program will stop running when the user enters the EXIT value.
"""


# 定義結束程式的常數
EXIT = -100


def main():
    print('Welcome to the narcissistic number checker!')

    while True:
        # 讀取使用者輸入
        n_str = input('n: ')
        n = int(n_str)

        # 檢查是否輸入結束值
        if n == EXIT:
            print('Have a good one!')
            break

        # 1. 取得位數 (N)
        # 可以直接利用字串長度，或是用迴圈計算
        length = len(n_str)

        # 2. 拆解位數並計算 N 次方和
        sum_val = 0
        temp_n = n

        # 使用題目提示的 // 與 % 邏輯
        while temp_n > 0:
            digit = temp_n % 10  # 取出最後一位數
            sum_val += (digit ** length)  # 累加該位數的 N 次方
            temp_n //= 10  # 去掉最後一位數

        # 3. 判斷並輸出結果
        if sum_val == n:
            print(str(n) + ' is a narcissistic number')
        else:
            print(str(n) + ' is not a narcissistic number')


if __name__ == '__main__':
    main()
