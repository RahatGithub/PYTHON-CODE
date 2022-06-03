# *args is used for passing variable number of arguments through a function/method
# *args is an optional argument. The program can be executed without this argument

def letterCount(*args):  # 'args' will always be received as a Tuple.
    for name in args:
        print(f"{len(name)} letters in {name}")
    print()

users = ["Rofiq", "Mursalin", "Monuwar", "Priyangshu", "Saiful"]
letterCount(*users)   # 'users' List will be unpacked and passed as n number of arguments where n = len(users)


# **kwargs is used for passing variable number of arguments with keywords, through a function/method
# **kwargs is an optional argument. The program can be executed without this argument
# **kwargs should always come after *args in the argument
def showHome(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} is from {value}")

info = {"Azad":"Khulna", "Belal":"Rajshahi", "Layek":"Sylhet"}
showHome(**info)     # 'info' Dictionary will be unpacked and passed as n number of arguments where n = len(info)
