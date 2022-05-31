def merge_sort(arr):
    if len(arr)<=1:
        return
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge_two_sorted_arr(left, right, arr)

def merge_two_sorted_arr(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i=j=k=0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k] = a[i]
            i+=1
            k+=1
        else:
            arr[k] = b[j]
            j+=1
            k+=1
    while i<len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k] = b[j]
        j+=1
        k+=1
    
array_set = [
    [3,2,6,1,5],
    [9,12,6,10,3,5],
    [1,18,9,3,6,27,15,12,21]
    ]

for arr in array_set:
    merge_sort(arr)
    print(arr)