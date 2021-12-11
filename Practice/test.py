class Node : 
    def __init__(self, data) :
        self.data = data
        self.next = None 


class LinkedList : 
    def __init__(self) :
        self.head = None
        self.tail = None 


    def append(self, data) :
        if self.head == None :
            self.head = Node(data)
            self.tail = self.head 
        else : 
            self.tail.next = Node(data) 
            self.tail = self.tail.next 

    def deleteFromPos(self, pos) :
        if self.head != None : 
            currentNode = self.head
            for i in range(1,pos-1) :
                if currentNode.next != None : 
                    currentNode = currentNode.next 
            currentNode.next = currentNode.next.next 


    def sort(self) :
        if self.head == None : 
            return 
        else : 
            currentNode = self.head 
            while currentNode : 
                checkNode = currentNode.next
                while checkNode : 
                    if currentNode.data > checkNode.data : 
                        currentNode.data, checkNode.data = checkNode.data, currentNode.data 
                    checkNode = checkNode.next 
                currentNode = currentNode.next 


    def display(self) :
        if self.head != None :
            currentNode = self.head 
            while currentNode : 
                print(currentNode.data, end=" --> ")
                currentNode = currentNode.next

l_list = LinkedList() 

values = [6, 2, 3, 1, 5, 8, 4, 7]

for value in values : 
    l_list.append(value)

l_list.sort()

print("Your linked list : ")
l_list.display()