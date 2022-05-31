class Node : 
  def __init__(self, data):
    self.data = data 
    self.prev = None 
    self.next = None 
  

class DoublyLinkedList : 

  def __init__(self):
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
  
  def SortedInsert(self, data) :
    if self.head == None : 
      self.InsertToStart(data)
    else : 
      node = Node(data)
      temp = self.head 
      pos = 1 
      flag = 0
      while temp != None : 
        if node.data < temp.data :
          self.InsertToPos(data, pos)
          flag = 1
          break
        pos += 1
        temp = temp.next 
      if flag == 0 : self.InsertToEnd(data)

  def Display(self) :
        if self.head == None : 
            print("The list is empty!")
        else :
            temp = self.head 
            while temp != None : 
                print(temp.data, end=" ")
                temp = temp.next


li = DoublyLinkedList()
values = [3, 5, 7, 9, 11]
for value in values : 
  li.InsertToEnd(value)

print("Before inserting : ")
li.Display(); print(" ")

num = int(input())
li.SortedInsert(num)

print("After inserting : ")
li.Display()