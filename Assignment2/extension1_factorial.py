"""
File: extension1_factorial.py
Name: 呂沅翰
-------------------
This program repeatedly asks the user to enter a number
and calculates the factorial of that number.

The result is printed to the console.
The program will stop running when the user enters the EXIT value.
"""


# 定義結束程式的常數
EXIT = -100


def main():
    print('Welcome to stanCode factorial master!')

    while True:
        # 讀取使用者輸入
        n = int(input('Give me a number, and I will list the answer of factorial: '))

        # 檢查是否輸入結束值
        if n == EXIT:
            break

        # 階乘運算邏輯
        # 0! 和 1! 的結果都是 1
        result = 1
        for i in range(1, n + 1):
            result *= i

        print('Answer: ' + str(result))

    # 離開迴圈後印出結束訊息
    print('------See ya!------')


if __name__ == '__main__':
    main()