"""Checking if the K-th bit (from left) of a binary string is SET or NOT SET (1 or 0)

   Also, we can check K-th bit from right by commenting out the line: k = str_len - k + 1"""

def KthBit(n, k):
    
    str_len = len(bin(n)[2:])
    
    k = str_len - k + 1    # Finding the position from left side as the next operation will count from right side. [ pos_left = len - pos_right + 1 ]
    
    if n & (1 << (k-1)):   # If this gives a value other then 0, then it is SET or 1 
        
        return "SET"
    
    else:                  # Else it is NOT SET or 0
        
        return "NOT SET" 
        

num, pos = map(int, input().split())
    
res = KthBit(num, pos) 
    
print(bin(num)[2:], res)