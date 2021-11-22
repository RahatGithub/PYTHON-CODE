"""Primality test using Fermat's Little Theorem

Time complexity: O(k log n) //n is the number to be checked and k is the number of repetitions 
This can be used for huge numbers. But, this is a probabilistic test. Chances are, you may hit the wrong one!"""

#***Not completed yet***
from random import randint

n = int(input())

a = randint(1,n)

check = pow(a,n-1)%n 

if check == 1: print("prime")

else : print("not prime")