# python3
__author__ = 'kwheelerj'

import sys


def is_balanced(string):
	stack = []
	index = 0
	for char in string:
		index = index + 1
		if char in ['[', '(', '{']:
			stack.append(char)
		elif char in [']', ')', '}']:
			if not stack:
				return str(index)
			top = stack.pop()
			if (top == '[' and char != ']') or (top == '(' and char != ')') or (top == '{' and char != '}'):
				return str(index)
		else:
			continue
	if not stack:
		return 'Success'
	else:
		return str(index)


if __name__ == "__main__":
	text = sys.stdin.read()
	# text = input()
	print(is_balanced(text))
