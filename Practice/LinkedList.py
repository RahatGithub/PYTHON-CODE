class LinkedList:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


node1 = LinkedList("Afghanistan")
node2 = LinkedList("India")
node3 = LinkedList("England")
node4 = LinkedList("Israel")

node1.nextNode = node3
node3.nextNode = node4 
node4.nextNode = node2

currentNode = node1
while True:
    print(currentNode.value, "->", end=" ")
    if currentNode.nextNode is None:
        print("None")
        break  
    currentNode = currentNode.nextNode
