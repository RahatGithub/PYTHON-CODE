# Decorators are used to enhance the functionality of a function without modifying it.
# Means, we can make the function do more, without changing its definition.

def wrapper(func):
    def wrap():
        print("************************************")
        func()
        print("************************************")
    return wrap


@wrapper    # this is equivalent to: welcome = wrapper(welcome).      [below the definition of welcome()]
def welcome():
    print("Welcome to the new environment")

welcome()