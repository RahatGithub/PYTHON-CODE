def getTime():
    """getTime() returns current date and time"""
    import datetime
    return datetime.datetime.now()

members = ["Ashfak", "Nafiz", "Omur", "Mustafiz"]
modes = ["Read(0), Write(1)"]
tasks = ["Push ups(0), Seat ups(1), Bench press(2)"]

base_dir = '../Documentation/TextFiles/'  # <base_dir> should be revised everytime the directory is changed/modified


# This portion should be run only once. Once the files are created then this portion will cause error.
######################################################################################################
try:
    for member in members:
        # Creating files named after every member. Here, 'x' is the 'exclusive file mode.
        with open(f"{base_dir}/{member}.txt", "x") as file:
            cur_time = getTime()
            file.write(f"{cur_time} >> {member} just joined!")
except:
    pass
######################################################################################################


cont = 'y'  # This variable stores the user's choice(y/n) whether he wants to continue or not.

while cont == 'y':
    member = input(f"Select member from {members}: ")
    mode = input(f"\nSelect mode from {modes}: ")

    if mode == "1":   # Write mode
        task = input(f"Select task from {tasks}: ")
        if task == '0': task = "Push ups"
        elif task == '1': task = "Seat ups"
        elif task == '2': task = "Bench press"
        with open(f"{base_dir}/{member}.txt", "a") as file:
            cur_time = getTime()
            file.write(f"\n{cur_time} >> {member} has done {task}")
            print("Task added successfully")

    elif mode == "0":  # Read mode
        with open(f"{base_dir}/{member}.txt", "r") as file:
            for line in file.readlines():
                print(line, end="")

    cont = input("\nDo you want to continue? (y/n): ")

