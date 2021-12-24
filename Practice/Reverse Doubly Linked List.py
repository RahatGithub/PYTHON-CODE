# To create a new node
class Node : 
    def __init__(self, data) :
        self.data = data
        self.prev = None
        self.next = None 

# To create new doubly linked list
class DoublyLinkedList : 

    def __init__(self) :
        # Initializing the head of the list with None
        self.head = None
    
    def InsertToStart(self, data) :
        node = Node(data)
        if self.head != None : 
            self.head.prev = node 
            node.next = self.head 
        self.head = node  

    def InsertToEnd(self, data) :
        node = Node(data)
        if self.head == None : 
            self.head = node
        else :
            temp = self.head 
            while temp.next != None : 
                temp = temp.next 
            temp.next = node 
            node.prev = temp
    
    def InsertToPos(self, data, pos) :
        if pos == 1 : 
            self.InsertToStart(data)
        else : 
            temp = self.head
            count = 1
            while count != pos : 
                temp = temp.next 
                count += 1
            if temp == None : 
                self.InsertToEnd(data)
            else : 
                node = Node(data)
                node.prev = temp.prev
                node.next = temp 
                temp.prev.next = node 
                temp.prev = node 

    def DeleteFromStart(self) :
        if self.head == None : 
            print("The list is empty!")
        elif self.head.next == None : 
            self.head = None 
        else : 
            self.head.next.prev = None 
            self.head = self.head.next 

    def DeleteFromEnd(self) :
        if self.head == None : 
            print("The list is empty!")
        elif self.head.next == None : 
            self.head = None 
        else : 
            temp = self.head 
            while temp.next != None : 
                temp = temp.next 
            temp.prev.next = None 
            temp.prev = None 

    def DeleteFromPos(self, pos) :
        if self.head == None : 
            print("The list is empty!")
        elif pos == 1 : 
            self.DeleteFromStart()
        else : 
            temp = self.head 
            count = 1
            while count != pos: 
                temp = temp.next 
                count += 1
            if temp.next == None : 
                self.DeleteFromEnd()
            else : 
                temp.prev.next = temp.next
                temp.next.prev = temp.prev 

    def Reverse(self) : 
        if self.head == None :
            print("The list is empty!")
        else :
            temp = self.head 
            while temp.next != None : 
                temp = temp.next 
            while temp != None : 
                print(temp.data, end=" ")
                temp = temp.prev 
            
            
            

    def Display(self) :
        if self.head == None : 
            print("The list is empty!")
        else :
            temp = self.head 
            while temp != None : 
                print(temp.data, end=" ")
                temp = temp.next



ll = DoublyLinkedList()
print("List values: ") 
values = list(map(int, input().split()))
for value in values : 
    ll.InsertToEnd(value)

print("Actual list: ")
ll.Display()
print("\nReversed list: ")
ll.Reverse()
