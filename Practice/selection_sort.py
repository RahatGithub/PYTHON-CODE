List = [int(x) for x in input().split()]

length = len(List)




for i in range(length-1):
    
    Min = min(List[i:])
    
    Min_index = List.index(Min)
    
    if not List[i] == Min: 
        
        List[i], List[Min_index] = List[Min_index], List[i] 
    

print("Sorted: ", List)
