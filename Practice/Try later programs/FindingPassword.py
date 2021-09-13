from itertools import permutations

n,k = [int(x) for x in input().split()]
arr=[]
for i in range(n):
    arr.append(int(input()))

perm = permutations(arr,k)

for p in perm:
    if p[0]==5:
        for i in range(k):
            print(int(p[i]),end='')
        print()