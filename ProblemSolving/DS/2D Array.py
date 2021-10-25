def hourglassSum(arr):
    
    maxSum = -100

    for row in range(4):

        for col in range(4):

            top = sum(arr[row][col:col+3])

            mid = arr[row+1][col+1]

            bottom = sum(arr[row+2][col:col+3])

            hourglass = top + mid + bottom

            maxSum = max(maxSum, hourglass)
            
    return maxSum
    

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(hourglassSum(arr))