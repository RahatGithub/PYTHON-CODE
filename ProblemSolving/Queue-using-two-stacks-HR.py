from collections import deque

D = deque()

for _ in range(int(input())):

    _input = list(map(int, input().split()))
    
    
    if _input[0] == 1: 
        
        D.append(_input[1])
    
    elif _input[0] == 2:
        
        D.popleft()
    
    else:
        
        print(D[0])