"""Example 1: Declaring an anonymous function named 'welcome' which
returns a welcome statement and also capitalizes the argument 'name'"""

name = "suhash"
welcome = lambda name : f"Welcome to my world Mr.{name.capitalize()}"
print(welcome(name))




"""Example 2: Declaring an anonymous function named 'access' which
returns a string either 'Allowed' or 'Restricted' based on the argument 'age'"""

access = lambda age : 'Allowed' if age>=18 else 'Restricted'
print("Entry", access(9))




"""Example 3: Declaring an anonymous function named 'factorial' which
returns the factorial of the number given as argument"""

factorial = lambda n : 1 if n==1 else n * factorial(n-1)
print(factorial(5))