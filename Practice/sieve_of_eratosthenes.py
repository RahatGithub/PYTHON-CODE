"""Sieve of Eratosthenes is an algorithm for finding the prime numbers in a segment [1,n]

Time complexity: O(n log(log n))"""


from math import isqrt                                             # isqrt(n) returns the integer square root of n

def primes_in_range(n):
     
    if n<=2: return []                                             # Since there is no prime numbers less than 2, it will return an empty list

    is_prime = [True]*(n+1)                                        # Set all values in a list to True. Initially, we are assuming, all numbers in this list are primes

    for i in range(2, isqrt(n)+1):                                 # We need to check from 2 to only the square root of the number

        if is_prime[i] == True:                                    # If 'i' is a prime number then we need to mark all its multiples as False, except itself

            for x in range(i*i, n+1, i):                           # We can check from i*i because all numbers less than i*i should have already marked. We'll iterate till 'n' by making 'i' leaps/steps each time.
                
                if not is_prime[x] == False: is_prime[x] = False   # If the number is not already marked as False, let's mark it as False 
    
    return [i for i in range(2,n+1) if is_prime[i] == True]        # Return all numbers from the list that are marked as True. Since we already know 0 and 1 are not primes, we started the loop from 2



if __name__ == '__main__':

    n = int(input("Enter a number: "))

    print(primes_in_range(n))

