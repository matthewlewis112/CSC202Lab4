#Create node
#Node functions as an individual unit in a linked list that points to the next node in the list
#Data is the value the node represents
#Next is the value of the next node
#Prev is the value of the previous node

class Node:
	def __init__(self, data = None, prev = None, next = None):
		self.data = data
        self.prev = prev
		self.next = next
	def __repr__(self):
		return "Data: " + self.data
