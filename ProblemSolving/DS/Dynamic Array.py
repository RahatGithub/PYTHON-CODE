n, q = map(int, input().split())

lastAnswer = 0

arr = list([] for i in range(n))
        
for i in range(q):
    
    indicator, x, y = map(int, input().strip().split())
    
    idx = ((x ^ lastAnswer) % n)
    
    if (indicator == 1):

        arr[idx].append(y)
    
    else:

        lastAnswer = arr[idx][y % len(arr[idx])]

        print(lastAnswer)