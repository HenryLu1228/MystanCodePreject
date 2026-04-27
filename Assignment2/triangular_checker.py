"""
File: extension3_triangular_checker.py
Name:呂沅翰
--------------------------
This program repeatedly asks the user to enter a number and checks
whether the number is a triangular number.

A triangular number (Tn) can be represented as a triangular arrangement
of points, where the first row contains one element and each subsequent
row contains one more element than the previous one.

The nth triangular number can be calculated using the formula:
Tn = n(n + 1) / 2.

The program will stop running when the user enters the EXIT value.
"""


# 定義結束程式的常數
EXIT = -100


def main():
    print('Welcome to the triangular number checker!')

    while True:
        # 讀取使用者輸入
        target = int(input('n: '))

        # 檢查是否輸入結束值
        if target == EXIT:
            print('Have a good one!')
            break

        # 判斷是否為三角形數的邏輯
        # 我們從小到大試探每個第 n 個三角形數，直到結果 >= target
        n = 1
        current_triangular_num = 0

        while current_triangular_num < target:
            current_triangular_num = n * (n + 1) / 2
            if current_triangular_num == target:
                # 找到了，是三角形數
                print(str(target) + ' is a triangular number')
                break
            n += 1

        # 如果迴圈結束後 current_triangular_num 已經超過 target 且不相等
        if current_triangular_num > target:
            print(str(target) + ' is not a triangular number')


if __name__ == '__main__':
    main()
