"""Converting a binary string to integer and vice versa"""

# Converting integer to binary string
def IntToBin(num):
    
    return str(bin(num))[2:]

# Converting binary string to integer
def BinToInt(s):
    
    return int(s,2)


# Taking the option as input (1 or 2)
n = int(input("Choose an option:\n\n1. Binary string to Integer \n2. Integer to Binary string\n>> "))

if n == 1:
    s = input()
    print(BinToInt(s))

elif n == 2:
    n = int(input())
    print(IntToBin(n))