from math import sqrt,ceil

def isPrime(n):

    for i in range(2, ceil(sqrt(n))):

        if n%i == 0 :
                
            return "no"
            
    return "yes"


t = int(input())

for _ in range(t):

    n = int(input())

    print(isPrime(n))