"""Counting the number of 0s/1s in the binary representation of a positive integer"""

# counting the number of 1s in the binary representation of num
def countbits(num):  
    
    if num > 0:
        
        count = 0
        
        while num:              # Repeat the operations until num==0 i.e. there are no '1's left in the binary representation of 'num'
            
            num = num & (num-1) # Each time after this operation, one '1' will be removed from the binary representation of 'num'
            
            count += 1          # We are counting the number of '1's that have been removed.
        
        return count            # This is our answer because we can remove '1's as many as they are present in the binary representation of 'num' 
    
    return "Give a valid input"


n = int(input("Please enter a positive integer: "))

ones = countbits(n)

string = bin(n)[2:]             # All binary strings start with '0b'. To avoid this, we are taking [2:] 

zeroes = len(string) - ones     # Number of zeroes = total bits - number of ones 