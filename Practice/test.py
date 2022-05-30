file = open("Documentation/TextFiles/introduction.txt", "r")

print(file.tell())  # printing the file pointer position

print(file.read(20))

print(file.tell())  # printing the file pointer position

print(file.read(10))

print(file.tell())  # printing the file pointer position

file.seek(0)

print(file.read(15))

file.close()