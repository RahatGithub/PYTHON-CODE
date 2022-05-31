num_of_row = int(input("Enter the number of rows: "))
tilt = input("Enter 0 or 1 for tilt position: ")

if tilt == '0': range = range(1, num_of_row)
elif tilt == '1': range = range(num_of_row, 0, -1)

if num_of_row > 0:
    try:
        for i in range: print("*" * i)
    except:
        print("Check your input and enter a valid one")
else:
    print("Give a valid input. Number of rows can't be less than or equal to zero")