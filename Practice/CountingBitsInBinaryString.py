"""Counting the number of 0/1s in the binary representation of a positive integer"""

# counting the number of 1s in the binary representation of num
def countbits(num):  
    
    if num > 0:
        
        count = 0
        
        while num:
            num = num & (num-1)
            count += 1
        
        return count 


    return "Give a valid input"


n = int(input("Please enter a positive integer: "))

ones = countbits(n)

string = str(bin(n))[2:]     # all binary strings start with '0b'. To avoid this, we are taking [2:] 

zeroes = len(string) - ones  # number of zeroes = total bits - number of ones 