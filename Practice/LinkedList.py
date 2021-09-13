class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value



class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.head 
            self.tail = node
            self.size += 1
    
    def __str__(self):
        values = []
        node = self.head 
        while node is not None:
            values.append(node.value)
            node = node.next
        return f"[{','.join(str(value) for value in values)}]"


my_list = DoubleLinkedList()
my_list.add(9)
my_list.add(2)
my_list.add(5)
my_list.add(1)

print(my_list)