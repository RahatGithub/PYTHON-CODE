from collections import deque

stack = deque([])

n = int(input())

for i in range(n):
    _input = [int(x) for x in input().split()]

    if _input[0] == 1:
        stack.append(_input[1])
    
    elif _input[0] == 2:
        stack.pop()
    
    else:
        print(max(stack))

