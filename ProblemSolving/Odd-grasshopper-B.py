t = int(input())

while t:
    
    init_pos, jumps = map(int, input().split())
    
    rem = jumps%4  #There is a repeating pattern after each 4 jumps
    
    
    if init_pos%2 == 0:
        
        if rem == 0: pos = init_pos
        
        elif rem == 1: pos = init_pos - jumps
        
        elif rem == 2: pos = init_pos + 1
        
        elif rem == 3: pos = init_pos + 1 + jumps
        
    else:
        
        if rem == 0: pos = init_pos
        
        elif rem == 1: pos = init_pos + jumps
        
        elif rem == 2: pos = init_pos - 1
        
        elif rem == 3: pos = init_pos - 1 - jumps
        
    
    print(pos)
    
    t -= 1