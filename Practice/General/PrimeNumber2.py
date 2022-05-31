""" Checking if a number is PRIME or not. 
    Time complexity: O(root(n)) """

def prime(n):

    from math import sqrt, ceil

    for i in range(1, ceil(sqrt(n))): #[1, root(n)]
        if n%i == 0 and not i==1:
            return 'Not prime' 
        
    return 'Prime' 


n = int(input())

print(prime(n))