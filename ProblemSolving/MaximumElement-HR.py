stack = []  

for _ in range(int(input())):
    
    _input = list(map(int, input().split()))
    
    if _input[0] == 1: 
        
        if stack: # If the stack isn't empty:
            stack.append(max(stack[-1], _input[1])) # Store the bigger one between the top element in stack and the new input value
                                                    # By doing this, we're always keeping the maximum element of the stack in its top. We only want the maximum value because 
                                                    # each time the query is 3, we need to print the maximum element in stack. Thus, we are doing it in O(1) instead of O(n)
            
        else: 
            stack.append(_input[1]) # If the stack is empty then push the input value
    
    elif _input[0] == 2: del stack[-1]  # stack.pop() would do the same but we don't need to get/store the removed value, that's why 
                                        # we are parmanently deleting the last element
    
    else: print(stack[-1])