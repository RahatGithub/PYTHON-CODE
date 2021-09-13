names = ["Shamim", "Lukman", "Nahiyan", "Rasel", "Pabel", "Showkot", "Ihtemad", "Salek", "Mrinmoy"]
print(names[2:6]) #prints values with index 2 to 5

group1 = names[0:3] #slice1
group2 = names[3:6] #slice2
group3 = names[6:9] #slice3
print("group1: ",group1,"group2: ",group2,"group3: ",group3)
print("slices from start to 3:",names[:3]) #slices from start to 3
print("slices from 3 to end:",names[3:]) #slice form 3 to end
print("Every second element:",names[::2]) #prints every second element
print(names[0:9:2]) #prints 0 to 8 with gap of 2 each time
print(names[0::4]) #prints from 0 to end with stepping 4
print(names[2:-3]) #2 is index when counting from start and -3 is index when counting from end



