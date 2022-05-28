# Opening the file in 'rt' mode, which is the default mode. The file will open in 'rt' mode even if we don't include it in the parameters. 
file = open("Documentation/TextFiles/introduction.txt", "rt")


# Reading first 5 characters of the file 
content = file.read(5)
print(content)


# Reading next 5 characters of the file 
content = file.read(5)
print(content) 
# Once first 5 characters are read, the file pointer reads the content from next character


# Reading the whole file 
content = file.read()
print(content)
# As 10 characters are already read, it will read the rest of the text

file.close()