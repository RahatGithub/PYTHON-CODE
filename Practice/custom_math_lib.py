import math


# Returns a list of all prime numbers from 2 to n
def primes_less_than(n):
    
    if n<=2: 
        return []

    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, math.isqrt(n)+1):
        if is_prime[i] == True:
            for x in range(i*i, n+1, i):
                is_prime[x] = False
    
    return [i for i in range(n+1) if is_prime[i] == True]


