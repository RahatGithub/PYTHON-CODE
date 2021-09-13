def Merge(a, b):
    
    len_a, len_b = len(a), len(b)
    
    index_a, index_b = 0, 0
    
    merged_list = []
    
    """Camparing elements of two sorted arrays and pushing them to the 
    merged list in accending order"""
    
    while index_a < len_a and index_b < len_b:
        
        if b[index_a] < b[index_b]:
            
            merged_list.append(a[index_a])
            
            index_a += 1
        
        else:
            
            merged_list.append(b[index_b])
            
            index_b += 1
            
    """___________________________________________________________"""
    
    
        
    """Pushing the remaining elements that are either in A or B"""
        
    if index_a < len_a: 
        
        merged_list.append(a[index_a:])
    
    elif index_b < len_b:
        
        merged_list.append(b[index_b:])
        
    """___________________________________________________________"""
    
    return merged_list



"""The actual merge sort with recursion"""


def Merge_Sort(List):
    
    if len(List) <= 1 :
    
        return List
    
    
    mid = len(List) // 2
    
    left = Merge_Sort(List[:mid])
    
    right = Merge_Sort(List[mid:])
    
    return Merge(left, right)




if __name__ == '__main__':
    
    List = [int(x) for x in input().split()]
    
    print(Merge_Sort(List))
    














    
    