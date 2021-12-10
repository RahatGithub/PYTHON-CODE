class LinkedList : 
    def __init__(self, value, nextNode=None) : 
        self.value = value
        self.nextNode = nextNode 


node1 = LinkedList("Bangladesh")
node2 = LinkedList("Pakistan")
node3 = LinkedList("China")
node4 = LinkedList("Saudi Arabia")
node5 = LinkedList("USA")

node1.nextNode = node3
node2.nextNode = node4
node3.nextNode = node2 
node4.nextNode = node5

currentNode = node1
while True : 
    print(currentNode.value, "->", end=" ")
    if currentNode.nextNode == None : 
        print("None")
        break 
    currentNode = currentNode.nextNode

