def readFile(n):

    """Doc: readFile(n) takes the number of characters to read as the function argument and prints the text"""
    with open("Documentation/TextFiles/introduction.txt", "r") as file:
        content = file.read(n)
        print(content)
        print(file.tell())

readFile(32)             # printing first 32 characters
readFile(104)            # printing first 104 characters

print(readFile.__doc__)  # printing the docstring of the readFile(n) function