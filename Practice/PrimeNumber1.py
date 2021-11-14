""" Checking if a number is PRIME or not. 
Time complexity: O(n) """

def prime(n):
    divisors = 0
    for i in range(1, n+1):
        if n%i == 0:
            divisors += 1
    
    print(divisors)

    if divisors == 2: 
        return True
    else: 
        return False


n = int(input())

print(prime(n))