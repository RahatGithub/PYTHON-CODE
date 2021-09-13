num = int(input("Please enter a number: "))
if num<0:
    print("Are you gone nuts?")
    if num>0:
        print("Not enough man")
        if num>40:
            print("You are so fit boy")
            if num>50:
                print("Half century!")
                if num>100:
                    print("ow, it's a century!")

age = int(input("Enter your age: "))
if age<0:
    print("Age must be a positive number")
else:
    if age>100:
        print("Age must be under 100")
    else:
        if age>90:
            print("90 years! That's really cool")
        else:
            if age>50:
                print("You just scored a half century")
            else:
                if age<50:
                    print("Long way to go")
                else:
                    print("Why don't you go and die...")

score = int(input("Your score: "))
if score<0:
    print("Enter a valid score")
elif score<33:
    print("You are fail, you MORON!")
elif score<50:
    print("Horrible result")
elif score<80:
    print("Keep trying")
else:
    print("Well done")