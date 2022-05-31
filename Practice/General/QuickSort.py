def Partition(L, low, high):

    pivot = L[high]

    i = low - 1

    for j in range(low, high):
        
        if L[j] < pivot:

            i += 1

            L[i], L[j] = L[j], L[i]
    
    L[i+1], L[high] = L[high], L[i+1]
    
    return i+1




def Quick_Sort(L, low, high):

    if low >= high:

        return 
    
    p = Partition(L, low, high)

    Quick_Sort(L, low, p-1)

    Quick_Sort(L, p+1, high)


if __name__ == "__main__":

    L = [int(x) for x in input().split()]

    Quick_Sort(L, 0, len(L)-1)

    print(L)