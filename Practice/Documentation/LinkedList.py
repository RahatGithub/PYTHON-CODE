# To create new node
class Node : 
    def __init__(self, data) :
        self.data = data
        self.next = None 
    

# To create new linked list
class LinkedList : 

    def __init__(self) :
        # Initializing both head and tail of the list with None
        self.head = None 
        self.tail = None 
    
    # Method to append new data/node in the list
    def append(self, data) :
        if self.head == None :  # If there is no head element; means if the list is empty
            self.head = Node(data) # Creating a new node and declaring it as the head of the list
            self.tail = self.head # As the head is the only element so the tail will also be the same
        else :
            self.tail.next = Node(data) # If head is not None then there must be a tail as well. 
                                        # So, the next node of the existing tail will be our new node.
            self.tail = self.tail.next  # Now, the tail will be the new node

    def display(self) :
        currentNode = self.head # Initially assigning the head node to the currentNode
        while currentNode : # While currentNode is not None
            print(currentNode.data, end=" ") # Print the value/data of that node
            currentNode = currentNode.next  # Now the currentNode will be the next node of already printed node


n = int(input("Number of nodes in your linked list: ")) 

l_list = LinkedList() # Make an instance of LinkedList class

for i in range(n) : 
    value = input() # Take an node value as input 
    l_list.append(value) # Append the value in the linked list 

print("Your linked list : ", end=" ")
l_list.display() # Desplay the linked list
