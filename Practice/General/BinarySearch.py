
def binary_search(input_list, value):
    low = 0
    high = len(input_list)-1 
    while(low <= high):
        mid = (low + high)//2
        
        if input_list[mid] == value:
            return mid
        elif input_list[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1
            

my_list = [1, 5, 6, 8, 9]
find_value = 8
print(binary_search(my_list, find_value))