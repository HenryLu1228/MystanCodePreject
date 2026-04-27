"""
File: replace_keyword.py
Name:
----------------------
This program demonstrates how to
replace an old word with a new word
in a given string by using the
replace() function.
"""


def main():
	old_s = input('old str: ')
	old_w = input('old word: ')
	new_w = input('new word: ')
	ans = replace(old_s,old_w,new_w)
	print(ans)

def replace(old_s,old_w,new_w):
	if old_w in old_s:
		ans = ''
		i = old_s.find(old_w)
		ans += old_s[:i]
		ans += new_w
		ans += old_s[i+len(old_w):]
		return ans
	else:
		return 'error'




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
