nums = [12, 45, 23, 87, 23, 45, 90, 117, 12]

# To push/append an element at the end of a list
nums.append(34)


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


# 
