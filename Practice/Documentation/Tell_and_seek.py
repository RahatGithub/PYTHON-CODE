file = open("Documentation/TextFiles/introduction.txt", "r")

print(file.tell())    # printing the file pointer position [it will print 0]

print(file.read(20))  # printing first 20 characters

print(file.tell())    # printing the file pointer position [it will print 20]

print(file.read(10))  # printing next 10 characters

file.seek(0)          # setting the file pointer position [it will set to 0]

print(file.read(15))  # read first 15 characters

file.close()