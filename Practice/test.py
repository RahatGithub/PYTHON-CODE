def readFile(characters):
    """readFile(n) takes the number of characters to read as the function argument and prints the text"""
    with open("Documentation/TextFiles/introduction.txt", "r") as file:
        content = file.read(characters)
        print(content)
        print(file.tell())

readFile(32)
readFile(104)

print(readFile.__doc__)