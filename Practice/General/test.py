def letterCount(**kwargs):  # 'args' will always be received as a Tuple.

    # for name in args:
    #     print(f"{len(name)} letters in {name}")

    for key,value in kwargs.items():
        print(f"{key} is from {value}")

users = ["Rofiq", "Mursalin", "Monuwar", "Priyangshu", "Saiful"]
info = {"Jamil":"Sylhet", "Hammad":"Khulna", "Rouf":"Dhaka"}
letterCount(**info)