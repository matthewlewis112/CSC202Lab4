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

#Implements ADT Ordered List
#Stores data in an ordered linked list
class OrderedList:
    #
    def __init__(self):
        pass
    #
    def __repr__(self):
        pass
    #
    def add(self,item):
        pass
    #
    def remove(self, item):
        pass
    #
    def search_forward(self, item):
        pass
    #
    def search_backward(self, item):
        pass
    #
    def is_empty(self):
        pass
    #
    def size(self):
        pass
    #
    def index(self, item):
        pass
    #
    def pop(self):
        pass
    #
    def pop(pos):
        pass
