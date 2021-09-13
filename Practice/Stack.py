class Stack: 
    
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

s1 = Stack()
s1.push("A")
s1.push("B")
s1.push("C")
s1.push("D")
