def merge_sort(dataset, key, descending=False):
    size = len(dataset)
    if size == 1:
        return dataset
    mid = size//2
    left = merge_sort(dataset[:mid], key, descending)
    right = merge_sort(dataset[mid:], key, descending)
    
    return merge(left, right, key, descending)

def merge(a, b, key, descending):
    len_a = len(a)
    len_b = len(b)
    sorted_list = []
    i = j = 0
    while i<len_a and j<len_b:
        if a[i][key]>=b[j][key]:
            if descending:
                sorted_list.append(a[i])
                i+=1
            else:
                sorted_list.append(b[j])
                j+=1
        else:
            if descending:
                sorted_list.append(b[j])
                j+=1
            else:
                sorted_list.append(a[i])
                i+=1
    while i<len_a:
        sorted_list.append(a[i])
        i+=1
    while j<len_b:
        sorted_list.append(b[j])
        j+=1
    
    return sorted_list

dataset = [
    
    {'name':'Christopher Henrick', 'age':38, 'work_hour':8},
    {'name':'Helebeen Jogasa', 'age':32, 'work_hour':9},
    {'name':'Mohanlal Chaubey', 'age':47, 'work_hour':5},
    {'name':'Magaleen Monitel', 'age':28, 'work_hour':12},
    {'name':'Belarus Chopol', 'age':30, 'work_hour':4},
    {'name':'Karaman Solte', 'age':21, 'work_hour':3}
    
    ]

print(merge_sort(dataset, 'work_hour'))





# =============================================================================
############################### Alternative:1 #################################
# =============================================================================

# =============================================================================
# class sort:
#     def merge_sort(self, dataset, key, descending=False):
#         self.key = key
#         self.descending = descending
#         if len(dataset) <= 1:
#             return dataset
#         
#         mid = len(dataset)//2
#         left = self.merge_sort(dataset[:mid], self.key, self.descending)
#         right = self.merge_sort(dataset[mid:], self.key, self.descending)
#     
#         return self.merge_two_sorted_list(left, right)
# 
#     def merge_two_sorted_list(self, a, b):
#         len_a = len(a)
#         len_b = len(b)
#         sorted_list = []
#         
#         i=j=0
#         while i<len_a and j<len_b:
#             if a[i][self.key]<=b[j][self.key]:
#                 if self.descending==True:
#                     sorted_list.append(b[j])
#                     j+=1
#                 else:
#                     sorted_list.append(a[i])
#                     i+=1
#             else:
#                 if self.descending==True:
#                     sorted_list.append(a[i])
#                     i+=1
#                 else:
#                     sorted_list.append(b[j])
#                     j+=1
#         while i<len_a:
#             sorted_list.append(a[i])
#             i+=1
#         while j<len_b:
#             sorted_list.append(b[j])
#             j+=1
#         
#         return sorted_list 
#             
# my_list = [
#     
#     {'name':'Omar Mukhtar', 'age':36, 'nationality':'Lybian'},
#     {'name':'Ali Zafar', 'age':26, 'nationality':'Pakistani'},
#     {'name':'Khabib Nurmagomedov', 'age':27, 'nationality':'Russian'},
#     {'name':'Shobuj Islam', 'age':51, 'nationality':'Bangladeshi'},
#     {'name':'Irfan Shukkur', 'age':47, 'nationality':'Indian'},
#     {'name':'Cadem Milow', 'age':17, 'nationality':'Brazilian'}
#     
#     ]
#     
# test = sort()
# 
# print(test.merge_sort(my_list, 'nationality'))
# =============================================================================
    
    
    


# =============================================================================
############################### Alternative:2 #################################
# =============================================================================

# =============================================================================
# def merge_sort(elements, key, descending=False):
#     size = len(elements)
# 
#     if size == 1:
#         return elements
# 
#     left_list = merge_sort(elements[0:size//2], key, descending)
#     right_list = merge_sort(elements[size//2:], key, descending)
#     sorted_list = merge(left_list, right_list, key, descending)
# 
#     return sorted_list
# 
#     
# def merge(left_list, right_list, key, descending=False):
#     merged = []
#     if descending:
#         while len(left_list) > 0 and len(right_list) > 0:
#             if left_list[0][key] >= right_list[0][key]:
#                 merged.append(left_list.pop(0))
#             else:
#                 merged.append(right_list.pop(0))
# 
#     else:
#         while len(left_list) > 0 and len(right_list) > 0:
#             if left_list[0][key] <= right_list[0][key]:
#                 merged.append(left_list.pop(0))
#             else:
#                 merged.append(right_list.pop(0))
# 
#     merged.extend(left_list)
#     merged.extend(right_list)
#     return merged
# 
# if __name__ == '__main__':
#     elements = [
#         { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#         { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
#     ]
# 
#     sorted_list = merge_sort(elements, key='time_hours', descending=True)
#     print(sorted_list)
# =============================================================================
    
    
    
    