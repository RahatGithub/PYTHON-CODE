""" Checking if a number is PRIME or not. 
Time complexity: O(n) """

def isPrime(n):
    divisors = 0
    for i in range(1, n+1): #[1,n]
        if n%i == 0:
            divisors += 1
    
    print(divisors)

    if divisors == 2: 
        return "Prime"
    else: 
        return "Not prime"


n = int(input())

print(isPrime(n))