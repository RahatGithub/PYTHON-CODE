"""deque methods..."""

from collections import deque 

li = [3,4,5,6,7]

d = deque(li)       # We can use other iterable too 

d.append(8)         # Pushing '8' to the end of the deque

d.appendleft(2)     # Pushing '2' to the beginning of the deque 

d.pop()             # Popping the last element from the deque 

d.popleft()         # Popping the first element from the deque

d.extend([7,8,9])   # Extends the deque by adding more elements to the end 

d.extendleft([0,1]) # Extends the deque by adding more elements to the start

d.rotate(2)         # Rotates the deque by shifting all the elements' positions to their right by 2

d.rotate(-1)        # Rotates the deque by shifting all the elements' positions to their left by 1


d = deque("Rahat", maxlen=5)  
# It sets the maximum length of the deque to 5. Now, if more elements are added then the 
# same amount of elements will be automatically removed from the other side of the deque



    



