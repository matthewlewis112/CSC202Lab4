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
        self.head = Node()
        self.tail = Node()
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
        for i in range(self.num_of_items -1):
            strReturn += ", " + str(temp.next)
            temp = temp.next
        return strReturn
    
    # Implemented by Yash Satyavarpu
    # Adds the given item to the Ordered List
    # Added return None to end funtion earlier
    def add(self, item):
        current = self.head
        previous = None
        stop = False

        if self.is_empty():
            self.head.data = item
            self.tail.data = item
            self.num_of_items += 1
            return None
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
            temp.next = self.tail
            self.head = temp
            self.num_of_items += 1
        elif item > self.tail.data:
            current.next = temp
            previous.next = current
        else:
            # Places item where it belongs. Inserts temp and updates connections.
            temp.next = current
            previous.next = temp
            self.num_of_items += 1


    #Implemented by Matthew Lewis
    #Removes the given item from the Order List
    def remove(self, item):
        if self.is_empty():
            return -1
        else:
            index = self.index(item)
            if index is -1:
                return -1
            else:
                if index is 0:
                    self.head = Node()
                    self.tail = Node()
                    self.num_of_items = 0
                elif index is 1:
                    self.head.next = Node()
                    self.tail = self.head
                    self.num_of_items = 1
                elif self.num_of_items -1 == index:
                    self.tail = self.tail.prev
                    self.num_of_items -= 1
                else:
                    temp = self.head
                    for i in range(index-1):
                        temp = temp.next
                    newNext = temp.next
                    temp.prev.next = newNext
                    self.num_of_items -= 1
            return index
    
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
            return False
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
        elif self.head.data == item:
            return 0
        else:
            index = 0
            current = self.head
            found = False
            stop = False
            while current != None and not found and not stop:
                index += 1
                if current.data == item:
                    return index
                else:
                    if current.data == None or current is None:
                        return -1
                    elif current.data > item:
                        stop = True
                    else:
                        current = current.next
            return -1
    
    #Implemented by Yash Satyavarpu
    #Removes and returns the last item in the list.
    def pop(self, pos = None):
            if pos is None:
                ans = self.tail.data
                self.remove(self.tail.data)
            else:
                if pos > self.size()/2:
                    if self.search_backward(list[pos]) is True:
                        ans = list[pos]
                        self.remove(list[pos])
                        return ans
                    else:
                        return -1
                elif pos < self.size()/2:
                    if self.search_forward(list[pos]) is True:
                        ans = list[pos]
                        self.remove(list[pos])
                        return ans
                    else:
                        return -1
                else:
                    return -1
            return ans
