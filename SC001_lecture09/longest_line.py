"""
File: longest_line.py
Name:
---------------------------
This program demonstrates how to
find the longest line in the file
romeojuliet.txt using Python.

By reading the file line by line,
we will practice comparing strings
and keeping track of the longest one.
"""

# This constant shows the file path to romeojuliet.txt
FILEPATH = 'text/romeojuliet.txt'


def main():
	f = open(FILEPATH, 'r')
	###########
	count = 0
	for line in f:
		count += 1
		if count == 1:
			longest_line = line
			longest_count = len(line)
		else:
			if longest_count < len(line):
				longest_line = line
				longest_count = len(line)
	print(longest_line)
	###########
	f.close()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
