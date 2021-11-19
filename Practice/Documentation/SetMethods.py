set1 = set()                           #Declare an empty set. Way: 1 

set2 = {}                              #Declare an empty set. Way: 2

ages = {14, 11, 15, 17, 20, 29}

length = len(ages)                     #Finds the length of the set

ages = sorted(ages)                    #Now 'ages' becomes a list with sorted values of set 'ages'

ages = set(ages)                       #Again 'ages' becomes a set, but this time it will print a sorted set because previously it was a sorted list

ages = {x*2 for x in ages}             #Set comprehension applied which doubled each element of 'ages' 

ages.add(55)                           #New element added to the set. Only one element can be added by '.add()'

ages.pop()                             #Pops off an element randomly. Only one at a time

ages.remove(58)                        #Removes the specific element

ages.discard(420)                      #Removes the specific element


""".remove() raises an error when the specified element doesn't exist in the given set,
but .discard() doesn't raise any error if the specified element is not present in the 
set and the set remains unchanged"""


ages.update({3, 4, 5})                 #Updating (inserting) the set with new elements

nums = [100, 200, 400]             

ages.update(nums)                      #Adding all elements from the list 'nums' to the set 'ages'


""".update() implies to any type of iterable. It modifies the main set. If some elements are 
already in the set then .update() will add only the new/unique ones. If nothing new/unique
then it will keep the set as it is."""


x = {"Sabbir", "Numan", "Jafar"}

y = {"Saiful", "Abrar", "Emon", "Numan"}

z = x.difference(y)                    #Returns the elements of 'x' that are not present in 'y'

z = x - y                              #Same as x.difference(y)


""".difference() doesn't modify the main set. It just simply returns a new set."""


x.difference_update(y)                 #Removes elements from 'x' that are not in 'y'


""".difference_update() does modify the main set.
Basically, A.difference_update(B) updates set A to A.difference(B)."""


z = x.union(y)                         #Returns a new set 'x union y'. It doesn't change the main sets 'x' and 'y'

z = x.intersection(y)                  #Returns a new set 'x intersection y'. It doesn't change the main sets 'x' and 'y'

x.intersection_update(y)               #Updates 'x' to only the common elements of 'x' and 'y'


"""Basically, A.intersection_update(B) updates set A to A.intersection(B)."""


x = {5, 14, 16, 12, 15}

y = {12, 16, 34, 51}

z = x.symmetric_difference(y)          #Returns all the elements of 'x' and 'y' except the common ones


"""Basically, A.symmetric_difference(B) is equivalent to A.union(B) - A.intersection(B).
It can be used when we want the elements which are either in A or in B, but not in both A and B."""


z = x.symmetric_difference_update(y)   #Updates set 'x' to the elements that are either in 'x' or in 'y'


"""Basically, A.symmetric_difference_update(B) updates set A to A.symmetric_difference(B)."""


z = x.issubset(y)                      #Returns: 'True' if 'x' is a subset of 'y', otherwise 'False'

z = x.issuperset(y)                    #Returns: 'True' if 'x' is a superset of 'y', otherwise 'False'

z = x.isdisjoint(y)                    #Returns: 'True' if 'x' and 'y' have nothing in common, otherwise 'False'

if x == y : print("Equal")             #Comparison between sets

ages.clear()                           #Clears all elements in the set 'ages'