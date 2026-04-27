"""
File: prime_checker.py
Name:呂沅翰
-----------------------
This program asks the user to enter a number and checks whether
the number is a prime number.

When the program starts, it first prints a welcome message to
the console. It then repeatedly prompts the user to enter an
integer greater than 1 and determines whether the number is prime.

The program will stop running when the user enters the EXIT value.
"""

EXIT = -100


def is_prime(num):
	"""判斷一個數字是否為質數"""
	if num <= 1:
		return False
	# 檢查從 2 到 num 的平方根之間是否有因數
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True


def main():
	print("Welcome to the prime checker!")

	while True:
		# 取得使用者輸入
		user_input = int(input("n: "))

		# 檢查是否為離開指令
		if user_input == EXIT:
			print("Have a good one!")
			break

		# 判斷並印出結果
		if is_prime(user_input):
			print(f"{user_input} is a prime number.")
		else:
			print(f"{user_input} is not a prime number.")


if __name__ == "__main__":
	main()