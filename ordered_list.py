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

# Implemented by Yash Satyavarpu
# Adds the given item to the Ordered List
    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            # Searches through list to find where item belongs.
            if current.data > item:
                stop = True
            else:
                previous = current
                current = current.next

        temp = Node(item)
        if previous is None:
            # If item is largest in the list, sets it as head.
            temp.next = self.head
            self.head = temp
            self.num_of_items += 1
        else:
            # Places item where it belongs. Inserts temp and updates connections.
            temp.next = current
            previous.next = temp
            self.num_of_items += 1
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
						rValue = temp.data
                        #Connect previous node to next node
                        temp.prev.next = temp.next
                        #Connect next node to previous node
                        temp.next.prev = temp.prev
                        temp.prev = None
                        temp.next = None
						return rValue
                    temp = temp.next

# Implemented by Yash Satyavarpu
# Returns True if item is in list, False if not
    def search_forward(self, item):
        # Cannot search an empty Ordered List
        if self.num_of_items == 0:
            return False
        else:
            current = self.head
            found = False
            stop = False
            while current != None and not found and not stop:
                if current.data == item:
                    found = True
                else:
                    if current.data > item:
                        stop = True
                    else:
                        current = current.next

            return found

    #Implemented by Matthew Lewis
    #Returns true if in list
    def search_backward(self, item):
        #Cannot remove from an empty Ordered List
        if self.num_of_items == 0:
            return Flase
        else:
            index = self.num_of_items - 1
            temp = self.tail
            if temp.data == item:
                return True
            else:
				temp = temp.next
				index -=1
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
            return -1
        else:
            index = self.num_of_items - 1
            temp = self.tail
            if temp.data == item:
                return index
            else:
                temp = temp.next
				index -=1
                while temp != None:
                    if temp.data == item:
                        return index
                    temp = temp.prev
                    index -= 1
<<<<<<< HEAD
                return None

#Implemented by Yash Satyavarpu
#Removes and returns the last item in the list.
=======
                return -1
    #
>>>>>>> 63323694df01f0ae01110777914749728316ebfb
    def pop(self):
        ans = self.tail.data
        temp = self.tail
        temp.prev.next = None
        self.num_of_items = self.num_of_items - 1
        return ans
#Implemented by Yash Satyavarpu
    def pop(self, pos):
        if pos > self.size()/2:
            if self.search_backward(list[pos]) is True:
                self.num_of_items = self.num_of_items - 1
                return self.remove(list[pos])
            else:
                return -1
        elif pos < self.size()/2:
            if self.search_forward(list[pos]) is True:
                self.num_of_items = self.num_of_items - 1
                return self.remove(list[pos])
            else:
                return -1
        else:
            return -1
