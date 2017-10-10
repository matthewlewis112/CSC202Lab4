#Course: 202-7
#Programmers:
#Yash Satyavarpu
#Matthew Lewis

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
		return str(self.data)

#Implements ADT Ordered List
#Stores data in an ordered linked list
#Head contains node with lowest value item
#Tail contains node with highest value item
#Num_of_items keeps track of the number of items in the Ordered List
class OrderedList:
    #Initializes OrderedList according to spec
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_items = 0
    #Implemented by Matthew Lewis
    #Converts Ordered List to string
    #Returns string of sequence of items in the Ordered List
    def __repr__(self):
        if self.head == None:
            return None
        else:
			temp = self.head
            strReturn = str(temp)
			temp = temp.next
            while temp != None:
                strReturn += ", " + str(temp)
			return strReturn
    #
    def add(self, item):
        pass
    #Implemented by Matthew Lewis
    #Removes the given item from the Order List
    def remove(self, item):
        #Cannot remove from an empty Ordered List
        if self.head == None:
            raise IndexError()
        else:
            temp = self.head
            if temp.data == item:
                self.head = self.head.next
            else:
                while temp != None:
                    if temp.data == item:
                        #Connect previous node to next node
                        temp.prev.next = temp.next
                        #Connect next node to previous node
                        temp.next.prev = temp.prev
                        temp.prev = None
                        temp.next = None
                    temp = temp.next

    #
    def search_forward(self, item):
        pass
    #Implemented by Matthew Lewis
    #Returns index of item
    def search_backward(self, item):
        #Cannot remove from an empty Ordered List
        if self.num_of_items == 0:
            return False
        else:
            index = self.num_of_items - 1
            temp = self.tail
            if temp.data == item:
                self.tail = self.tail.prev
                index -= 1
            else:
                while temp != None:
                    if temp.data == item:
                        return True
                    temp = temp.prev
                    index -= 1
                return False

    #Implemented by Matthew Lewis
    def is_empty(self):
        return self.num_of_items == 0
    #Implemented by Matthew Lewis
    def size(self):
        return self.num_of_items
    #Implemented by Matthew Lewis
    def index(self, item):
        #Cannot remove from an empty Ordered List
        if self.num_of_items == 0:
            return None
        else:
            index = self.num_of_items - 1
            temp = self.tail
            if temp.data == item:
                self.tail = self.tail.prev
                index -= 1
            else:
                while temp != None:
                    if temp.data == item:
                        return index
                    temp = temp.prev
                    index -= 1
                return None
    #
    def pop(self):
        pass
    #
    def pop(pos):
        pass
