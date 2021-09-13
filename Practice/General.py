
def TowerOfHanoi(num_of_disks, source, destination, auxiliary):
    
    
    if num_of_disks > 0:
        
        TowerOfHanoi(num_of_disks - 1, source, auxiliary, destination)
        
        print("Move a disk from", source, "to", destination)
        
        TowerOfHanoi(num_of_disks -1, auxiliary, destination, source)
    

TowerOfHanoi(5, '1st', '2nd', '3rd')

