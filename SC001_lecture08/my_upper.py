"""
File: my_upper.py
Name:
----------------------
This program demonstrates how the
Python built-in method s.upper()
can be implemented.

By recreating its behavior step by
step, we will better understand how
string methods work internally.
"""


def main():
	s = '123JeRrY123'
	print(upper(s))


def upper(s):
	ans = ""
	for i in range(len(s)):
		if s[i].islower():
			ans += s[i].upper()
		else:
			ans += s[i]

	return ans

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #


if __name__ == '__main__':
	main()
