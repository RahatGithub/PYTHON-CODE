t = int(input())

for _ in range(t):
    
    keyboard, string, time, current_position = input(), input(), 0, 0
    
    for i in range(0, len(string)):
        
        new_position = keyboard.index(string[i]) 
        
        if not i==0:
            
            time += abs(new_position - current_position)
            
        current_position = new_position
    
    print(time)