# python3
__author__ = 'kwheelerj'


import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size


class Tree:
	def __init__(self, number_of_nodes, data):
		self.nodes = [None] * number_of_nodes
		for i in range(number_of_nodes):
			self.nodes[i] = Node(i)

		for child_index in range(number_of_nodes):
			parent_index = data[child_index]
			if parent_index == -1:
				self.root = self.nodes[child_index]
			else:
				self.nodes[parent_index].add_child(self.nodes[child_index])


def compute_height(node):
	if not node:
		return 0
	child_node_heights = []
	if not node.children:
		return 1
	for child_node in node.children:
		child_node_heights.append(compute_height(child_node))
	return 1 + max(child_node_heights)


class Node:
	def __init__(self, number):
		self.number = number
		self.children = []

	def add_child(self, node):
		self.children.append(node)

	def __str__(self):
		_string = ""
		_string += "Node({0})\n".format(self.number)
		for child in self.children:
			_string += "\t child_node({0})\n".format(child.number)
		return _string


def main():
	number_of_nodes = int(input())
	data = list(map(int, input().split()))
	# number_of_nodes = int(sys.stdin.readline())
	# data = list(map(int, sys.stdin.readline().split()))
	tree = Tree(number_of_nodes, data)
	print(compute_height(tree.root))


threading.Thread(target=main).start()
