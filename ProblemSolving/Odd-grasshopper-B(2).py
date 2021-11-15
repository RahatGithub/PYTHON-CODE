functions = [
    lambda x : 0,
    lambda x : x,
    lambda x : -1,
    lambda x : -x-1
]

t = int(input())

for _ in range(t):
    
    init_pos, jumps = map(int, input().split())
    
    d = functions[jumps%4](jumps)   #The remainder of jumps/4 acts like the serial no. of the functions. If jumps%4==i then it will use the i-th lambda function
    
    if init_pos%2 == 0: print(init_pos - d)
    
    else: print(init_pos + d)