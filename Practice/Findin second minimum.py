arr = [2, 1, 4, 5, 6, 7, 11, 3, 9]

for i in range(len(arr)-1):

    if arr[i] > arr[i+1]:

        temp = arr[i+1]                
        arr[i+1] = arr[i]               
        arr[i] = temp                   

print(arr[1])