visitors_ages = [12, 11, 45, 16, 21, 31, 51, 21, 22, 26]

audience_ages = list(filter(lambda age : age>=18, visitors_ages))  # filter() takes two arguments- a function and an iterable
                                                                   # filter() returns an object. Here, list() is used so that the 'audience_ages' is stored as a list
                                                                   # if the function returns True then the value will be added to 'audience_ages'

print(audience_ages)    # output: [45, 21, 31, 51, 21, 22, 26]     # only these values have returned True for the condition 'age >= 18'