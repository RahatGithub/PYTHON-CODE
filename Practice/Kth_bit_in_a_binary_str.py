"""Checking if the K-th bit of a binary string is SET or NOT SET (1 or 0)"""

def KthBit(n, k):
    
    if n & (1 << (k-1)):   # If this gives a value other then 0, then it is SET or 1 
        
        return "SET"
    
    else:                  # Else it is NOT SET or 0
        
        return "NOT SET" 
        

num, pos = map(int, input().split())

res = KthBit(num, pos) 

print(bin(num)[2:], res)