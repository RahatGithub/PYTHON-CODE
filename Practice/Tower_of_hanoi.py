
def TowerOfHanoi(n, src, aux, des):
    
    
    if n > 0:
        
        TowerOfHanoi(n - 1, src, des, aux)
        
        print("Move a disk from", src, "to", des, "\n")
        
        TowerOfHanoi(n -1, aux, src, des)
    

TowerOfHanoi(4, 'Left', 'Mid', 'Right')