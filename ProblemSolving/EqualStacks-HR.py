n1, n2, n3 = map(int, input().split())
H1 = list(map(int, input().split()))[::-1]
H2 = list(map(int, input().split()))[::-1]
H3 = list(map(int, input().split()))[::-1]

sum_h1 = sum(H1)
sum_h2 = sum(H2)
sum_h3 = sum(H3)

while not (sum_h1 == sum_h2 and sum_h2 == sum_h3):
    if sum_h1 > sum_h2 or sum_h1 > sum_h3:
        t = H1.pop()
        sum_h1 -= t
    if sum_h2 > sum_h1 or sum_h2 > sum_h3:
        t = H2.pop()
        sum_h2 -= t
    if sum_h3 > sum_h1 or sum_h3 > sum_h2:
        t = H3.pop()
        sum_h3 -= t
print(sum_h1)
