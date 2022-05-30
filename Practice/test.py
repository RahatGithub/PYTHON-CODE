def getTime():
    import datetime
    return datetime.datetime.now()

usersList = ["Ashfak", "Nafiz", "Omur", "Mustafiz"]
modes = ["Read(0), Write(1)"]
tasks = ["Push ups(0), Seat ups(1), Bench press(2)"]

for user in usersList:
    with open(f"documents/{user}.txt", "x") as file:
        cur_time = getTime()
        file.write(f"{cur_time} >> {user} just joined!")

cont = 'y'

while cont == 'y':
    user = input(f"Select user from {usersList}: ")
    mode = input(f"\nSelect mode from {modes}: ")
    if mode == "1":
        task = input(f"Select task from {tasks}: ")
        if task == '0': task = "Push ups"
        elif task == '1': task = "Seat ups"
        elif task == '2': task = "Bench press"
        with open(f"documents/{user}.txt", "a") as file:
            cur_time = getTime()
            file.write(f"\n{cur_time} >> {user} has done {task}")
            print("Task added successfully")

    elif mode == "0":
        with open(f"documents/{user}.txt", "r") as file:
            for line in file.readlines():
                print(line, end="")

    cont = input("\nDo you want to continue? (y/n): ")
