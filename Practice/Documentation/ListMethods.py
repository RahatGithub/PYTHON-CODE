nums = [12, 45, 23, 87, 23, 45, 90, 117, 12]

# To push/append an element at the end of a list
nums.append(34)


# To insert an element at a specific index. syntax: list.insert(index, value)
nums.insert(3, 100)


# To pop an element of the list. If the index is not given as parameter then it pops off the last element of the list
nums.pop(2)


# To remove a specific element of a list
friends = ['Junaed', 'Kabir', 'Shaikat', 'Monon']
friends.remove('Shaikat')


# To copy 'nums' list to 'nums2' variable. As lists are mutable objects, if it was 'nums2 = nums' then applying a method on one of them 
# will automatically affect the other. That's why we take a copy of 'nums' as 'nums2' and change it as our wish without affecting 'nums'. 
nums2 = nums.copy()


# Returns number of occurrences of an element. Returns 0 if the desired element/value is missing
twelve = nums.count(12)


# Extends a list. Adds all elements of a list to another list. Here, the new value of myFavCars is, ['BMW', 'Tesla', 'Marcedes-Benz', 'Toyota', 'Hyundai', 'Tata']
myFavCars = ['BMW', 'Tesla', 'Marcedes-Benz']
carsInMarket = ['Toyota', 'Hyundai', 'Tata']
myFavCars.extend(carsInMarket)


# Spread operator (*) is used for unpacking iterables
summerFruits = ['Mango', 'Jackfruit']
winterFruits = ['Apple', 'Orange']
allFruits = [*summerFruits, *winterFruits, 'Guava', 'Papaya']


# To find the index of a specific element's first occurrance. Throws an error if the element is missing in the list
allFruits.index('Orange')
<<<<<<< HEAD


# To reverse the order of the list 
allFruits.reverse()


# To sort the list
allFruits.sort()


# Deletes an element or some elements from the list. 
del allFruits[3]    # Deletes the element having index 3
del allFruits[2:5]  # Deletes from 2nd to 4th element 

# Clears all the elements from the list
allFruits.clear()
=======
>>>>>>> 61f681f0966cca2933e4fd456403a14f6fbed087
