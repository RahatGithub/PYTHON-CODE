"""Checking if the K-th bit of a binary string is SET or NOT SET (1 or 0)"""

def KthBit(n, k):
    
    if n & (1 << (k-1)):   # It will have a value except 0 only for 1s 
        
        return "SET"
    
    else:                  # Else it is 0
        
        return "NOT SET" 
        

num, desiredPosition = map(int, input().split())

res = KthBit(num, desiredPosition)

print(bin(num)[2:], res)