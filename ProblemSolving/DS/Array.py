def reverseArray(array):

    array = array[::-1]             #Reassigned the reversed array in 'array'

    print(*array)                   #Printing all elements separated by space


N = int(input())                    #Taking input of the length of array

array  = input().split()            #Taking input of the array in one line, separated by space

reverseArray(array)