# Import math Library
import math


# Rounds a number up to the nearest integer:
math.ceil(3.1416)   # Result: 4



# Rounds a number down to the nearest integer:
math.floor(3.1416)   # Result: 3



# Number of ways to choose k elements from n elements
n, k = 10, 4
math.comb(n, k)  # Result: 45



# Returns the number of ways to choose k items from n items with order and without repetition:
n, k = 10, 4
math.perm(n, k)   # Result: 5040



# Converts angles from radians to degrees:
math.degrees(8.90)  # Result: 509.9324376664327



# Converts angles from degrees to radians:
math.radians(180)   # Result: 3.141592653589793



# Returns the factorial of a number:
math.factorial(5)   # Result: 120



# Returns the value(in float) of the first parameter and the sign of the second parameter
math.copysign(4, -1)  # Result: -4.00



# Calculates the Euclidean distance between two points/coordinates p and q:
p,q = [3,3], [6,12]  # value of p and q can be lists or tuples and should have same dimensions
math.dist(p,q)       # Result: 9.486832980505138



# Returns the exponential of the specified value, int other words- e raised x:
x = 65
math.exp(x)   # Result: 1.6948892444103338e+28



# Returns the absolute value of a number in float:
math.fabs(-3)   # Result: 3.0



# Returns the GCD of given numbers:
math.gcd(5,10,15,20)   # Result: 5



# Compares the closeness of two values:
math.isclose(1.233, 1.24)   # Result: False
math.isclose(1.233, 1.233000001)   # Result: True



# Returns the natural logarithm of different numbers:
math.log(2.7183)   # Result: 1.0000066849139877



# Returns the base-10 logarithm of different numbers:
math.log10(2.7183)   # Result: 0.43429738512450866



# Returns the base-2 logarithm of different numbers:
math.log2(2.7183)   # Result : 1.4427046851812222



# Returns the value(in float) of x raise to y:
x, y = 2, 4
math.pow(x,y)   # Result: 16.0



# Returns the product of all values in an iterable:
val = (3,4,2,5)  # It could be a LIST or SET also
math.prod(val)   # Result: 120