# python3
__author__ = 'kwheelerj'


import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size


class Tree:
	def __init__(self, number_of_nodes, data):
		self.number_of_nodes = number_of_nodes
		self.all_nodes = [None] * self.number_of_nodes

		for index in range(self.number_of_nodes):
			number = data[index]
			# print(index)
			# print(number)

			if number == -1:
				if self.all_nodes[index] is None:
					self.root = Node(index)
					self.all_nodes[index] = self.root
				else:
					self.root = self.all_nodes[index]
				continue

			parent_node = Node(number)
			child_node = Node(index)

			# print(str(parent_node not in self.all_nodes))
			if self.all_nodes[number] is None:
				self.all_nodes[number] = parent_node
			else:
				parent_node = self.all_nodes[number]

			# print(str(child_node not in self.all_nodes))
			if self.all_nodes[index] is None:
				self.all_nodes[index] = child_node
			else:
				child_node = self.all_nodes[index]

			# parent_node.add_child(child_node)
			self.all_nodes[number].add_child(self.all_nodes[index])

		# for node in self.all_nodes:
		# 	print(node)


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
	# number_of_nodes = int(input())
	# data = list(map(int, input().split()))
	number_of_nodes = int(sys.stdin.readline())
	data = list(map(int, sys.stdin.readline().split()))
	tree = Tree(number_of_nodes, data)
	print(compute_height(tree.root))


threading.Thread(target=main).start()
