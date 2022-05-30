def getTime():
    import datetime
    return datetime.datetime.now()

usersList = ["Ashfak", "Nafiz", "Omur", "Mustafiz"]
modes = ["Read, Write"]
tasks = ["Push ups, Seat ups, Bench press"]

for user in usersList:
    with open(f"Documentation/TextFiles/{user}.txt", "x") as file:
        cur_time = getTime()
        file.write(f"{cur_time} >> {user} just joined!")

user = input(f"Select user from {usersList}: ")
mode = input(f"Select mode from {modes}: ")
if mode == "Write":
    task = input(f"Select task from {tasks}: ")
    with open("Documentation/TextFiles/{user}.txt", "a") as file:
        cur_time = getTime()
        file.write(f"{cur_time} >> {user} has done {task}")
elif mode == "Read":
    with open(f"Documentation/TextFiles/{user}.txt", "r") as file:
        for line in file.readlines():
            print(line)

