import random

customers = ["Harun", "Tamim", "Yousuf", "Mohonlal", "Jaygirder"]

for i in range(10):
    winner = random.choice(customers)
    print(winner)
    # The argument of choice() method has to be an iterative like Lists or Tuples.
    # Sets or Dictionaries has to be converted into a List first in order to use.
    # e.g. if 'customers' was a Dictionary then, winner = random.choice(list(customers))