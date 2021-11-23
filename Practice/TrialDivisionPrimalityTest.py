"""Primality test using Trial Division Method

Time complexity: O(root(n))
Using this is ok for slightly bigger numbers but not for too large numbers"""

from math import ceil, sqrt

def isPrime(n):
    if n==1: return "no"

    for i in range(2,ceil(sqrt(n))+1):
        if n%i == 0: return "no"
    
    return "yes"


t = int(input())

for _ in range(t):
    n = int(input())
    print(isPrime(n))