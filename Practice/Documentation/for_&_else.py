students = ["Noyon", "Samadul", "Probin", "Choyon"]

name = input("Type the student name that you want to search: ")
for st in students:
    if st == name:
        print(f"Found {st}!")
        break

# If the whole for loop iterates without any intervension/break then the 'else' part will execute
else:
    print("student not found!")