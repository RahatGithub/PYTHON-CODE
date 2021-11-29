def isBalanced(string):
    
    brackets = {'(':')', '{':'}', '[':']'}
    
    check = []
    
    for char in string:
        
        if char in "({[": 
            
            check.append(char) 
        
        else:
            
            if check:
                
                if brackets[check[-1]] == char: del check[-1]   
                    
                else: return "NO"
                
            else: return "NO"

    return "NO" if check else "YES"



for _ in range(int(input())):
    
    string = input()
    
    print(isBalanced(string))