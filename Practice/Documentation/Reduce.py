# reduce() returns a value by processing an iterable

from functools import reduce

numbers = [4, 12, 5, 8, 9, 3]

sum_of_numbers = reduce(lambda x,y : x+y, numbers)  # the lambda function takes two arguments and returns their sum.
                                                    # when 'numbers' List is passed through the lambda function, it takes each pair of consecutive elements and returns their sum. Thus, finally returns the sum of the whole List

print(sum_of_numbers)