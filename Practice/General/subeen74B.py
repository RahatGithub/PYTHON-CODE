text = input("enter a text : ")

last_index = len(text)-1

rev_text = text[last_index::-1]

if text == rev_text: 
    print("Pelindrome")
    
else:
    print("Not pelindrome")