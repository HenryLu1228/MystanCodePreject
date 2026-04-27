"""
File: extension2_number_checker.py
Name:呂沅翰
------------------------
This program repeatedly asks the user to enter a number and checks
whether it is a perfect, deficient, or abundant number.

A perfect number is equal to the sum of all its factors excluding
itself. An abundant number has a factor sum greater than the number
itself, while a deficient number has a factor sum smaller than the number.

The program will stop running when the user enters the EXIT value.
"""


# 定義結束程式的常數
EXIT = -100


def main():
    print('Welcome to the number checker!')

    while True:
        # 讀取使用者輸入
        n = int(input('n: '))

        # 檢查是否輸入結束值
        if n == EXIT:
            print('Have a good one!')
            break

        # 計算真因子的總和
        # 真因子定義：除了數字本身以外的因數
        sum_of_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_of_divisors += i

        # 判斷數字類型並輸出
        if sum_of_divisors == n:
            print(str(n) + ' is a perfect number')
        elif sum_of_divisors > n:
            print(str(n) + ' is a abundant number')
        else:
            print(str(n) + ' is a deficient number')


if __name__ == '__main__':
    main()
