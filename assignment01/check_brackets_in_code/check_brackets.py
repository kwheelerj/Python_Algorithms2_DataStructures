# python3
__author__ = 'kwheelerj'

import sys


def is_balanced(string):
	stack = []
	index = 0
	for char in string:
		index += 1
		if char in ['[', '(', '{']:
			stack.append((char, index))
		elif char in [']', ')', '}']:
			if not stack:
				return str(index)
			top, _index = stack.pop()
			if (top == '[' and char != ']') or (top == '(' and char != ')') or (top == '{' and char != '}'):
				return str(index)
		else:
			continue
	if not stack:
		return 'Success'
	else:
		# print(stack[0])
		return stack[0][1]


if __name__ == "__main__":
	text = sys.stdin.read()
	# text = input()
	print(is_balanced(text.strip()))
