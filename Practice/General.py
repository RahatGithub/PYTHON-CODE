from math import ceil

row, col = [int(x) for x in input().split()]

drops = ceil(row/2) * ceil(col/2)

print(drops)