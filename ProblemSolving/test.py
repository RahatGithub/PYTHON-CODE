def twoStacks(a, b, maxSum):

    total_removed = count = 0
    
    while not (len(a) == len(b) == 0) : 
        
        if (a and b) and min(a[-1],b[-1]) == a[-1] :       
            total_removed += a.pop()
            if total_removed <= maxSum : count += 1
            else : return count 
        
        if (a and b) and min(a[-1],b[-1]) == b[-1] :           
            total_removed += b.pop()
            if total_removed <= maxSum : count += 1
            else : return count 
        
        if b == [] and not a == [] :
            total_removed += a.pop()
            if total_removed <= maxSum : count += 1
            else : return count 
        
        if a == [] and not b == [] :
            total_removed += b.pop()
            if total_removed <= maxSum : count += 1
            else : return count 
            
    return count
        

for _ in range(int(input())):

    n, m, maxSum = map(int, input().split())
    
    a = list(map(int, input().split()))[::-1]
    
    b = list(map(int, input().split()))[::-1]
    
    print (twoStacks(a, b, maxSum)) 