def hourglassSum(arr):
    
    maxSum = -100                                           #let maxSum be anything smaller then -63 [-9*7 = -63]

    for row in range(4):                                    #Don't need to check all 36(6X6) elements; just checking 16(4X4) elements

        for col in range(4):

            top = sum(arr[row][col:col+3])                  #Storing the sum of top column in 'top'

            mid = arr[row+1][col+1]                         #Storing the mid element in 'mid'

            bottom = sum(arr[row+2][col:col+3])             #Storing the sum of bottom column in 'bottom'

            hourglass = top + mid + bottom

            maxSum = max(maxSum, hourglass)                 #If maxSum is already greater then hourglass then fine, otherwise reassign maxSum as hourglass
            
    return maxSum
    

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))    #Taking input of 2D array

print(hourglassSum(arr))