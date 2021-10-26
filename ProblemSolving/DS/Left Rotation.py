n,d = map(int, input().split())

arr = list(map(int, input().split()))

if not d == n:
    
    arr = arr[d:] + arr[:d]
    
print(*arr)