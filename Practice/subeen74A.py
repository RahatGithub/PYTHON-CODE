text = input("Enter a text : ")

max_index = len(text) - 1 

for index in range(max_index):

    first_char = text[index]
    
    second_char = text[index + 1]
    
    text = text[index:index + 1].replace(second_char, first_char, 1) 
    
    text = text[index:index + 1].replace(first_char, second_char, 1) 
    
print(text)