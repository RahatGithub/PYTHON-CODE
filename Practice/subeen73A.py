text = input("Enter a text: ")

cap, low, num, others = [], [], [], []


"""Checking each character and pushing it to its respective list"""
for c in text:

    if c >= 'A' and c <= 'Z': cap.append(c)

    elif c >= 'a' and c <= 'z' : low.append(c)
    
    elif c >= '0' and c <= '9' : num.append(c)
    
    else : others.append(c)


"""Iterating each list and printing one list in each line"""
for each_list in cap, low, num, others: 
    for char in each_list : print(char, end="")
    print() 