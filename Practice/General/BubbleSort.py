array = [6, 2, 5, 7, 1, 4, 9, 3, 8]

len = len(array)

for i in range(len-1, 0, -1):
    for j in range(i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)


# =============================================================================
# # OPPOSITE WAY ITERATION
# array = [2, 5, 6, 1, 8, 7, 4, 9, 3]
# 
# len = len(array)
# 
# for i in range(0, len-1):
#     for j in range(len-1, 0, -1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#             
# print(array)
# =============================================================================
