def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))

terms = 10

for i in range(terms):
    print(fibo(i))