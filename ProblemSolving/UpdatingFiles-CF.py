t = int(input())

for _ in range(t):
    
    computers, cables = map(int, input().split())
    
    ready, hours = 1, 0
    
    while ready < computers:
        
        ready += min(ready, cables)
        hours += 1
            
        
    print(hours)