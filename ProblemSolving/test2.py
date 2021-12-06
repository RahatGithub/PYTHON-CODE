def isSingle(nums) : 
    z = 0
    for num in nums : 
        z = z ^ num   
    return z

nums = list(map(int, input().split()))

print(isSingle(nums))
