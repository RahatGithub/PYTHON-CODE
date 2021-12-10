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
            print(currentNode.data, end=" -> ") # Print the value/data of that node
            currentNode = currentNode.next  # Now the currentNode will be the next node of already printed node


    def insertAfter(self, existingValue, data) :
        if self.head == None : 
            pass
        else : 
            currentNode = self.head 
            while currentNode.data != existingValue : 
                currentNode = currentNode.next 
            newNode = Node(data)
            newNode.next = currentNode.next 
            currentNode.next = newNode 


    def insertAfterPos(self, pos, data) : 
        if self.head == None : 
            pass
        else : 
            count = 1
            currentNode = self.head
            while count != pos : 
                currentNode = currentNode.next 
                count += 1
            newNode = Node(data)
            newNode.next = currentNode.next 
            currentNode.next = newNode 

    
    def insertBefore(self, existingValue, data) :
        if self.head == None : 
            pass 
        else : 
            currentNode = self.head 
            # try an alternative to check currentNode.next.data 
            while currentNode.next.data != existingValue : 
                currentNode = currentNode.next 
            newNode = Node(data)
            newNode.next = currentNode.next 
            currentNode.next = newNode 
 
    ############# DIAGONOSIS REQUIRED !!! ##############
    def insertAtPos(self, pos, data) :
                if self.head == None : 
                    pass
                else : 
                    count = 1
                    currentNode = self.head
                    while count < pos-1 : 
                        currentNode = currentNode.next 
                        count += 1
                    newNode = Node(data)
                    newNode.next = currentNode.next 
                    currentNode.next = newNode 


values = ["Afghanistan", "Bangladesh", "India", "Pakistan"]
l_list = LinkedList()
for i in range(len(values)) : 
    value = values[i]  
    l_list.append(value)  

l_list.insertAfter("India", "Japan")
l_list.insertAfterPos(3, "New zealand")
l_list.insertBefore("India", "Canada")
l_list.insertAtPos(3, "Brazil")

print("Your linked list : ", end=" ")
l_list.display() # Desplay the linked list


