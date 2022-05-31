# Finding GCD of two numbers using Euclidean algorithm. 

# Time complexity: O(log n) where n = min(a,b)

def gcd(a, b):
    
    if b==0: return a
    
    else: return gcd(b, a%b)
    

num1,num2 = map(int, input().split())

res = gcd(num1,num2)

print(res)