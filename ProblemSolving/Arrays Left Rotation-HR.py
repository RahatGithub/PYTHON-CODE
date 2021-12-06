from collections import deque

def Rotate(arr, d) : 
    
    n = len(arr)
    arr = deque(arr)
    
    if not n == d :
        arr.rotate(-d)
      
    return list(arr)
    

arr = list(map(int, input().split()))
d = int(input())
print(*Rotate(arr,d))