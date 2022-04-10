favFruits = {'Arnold':'Mango', 'Russel':'Strawberry', 'Peter':'Apple', 'Sam':'Banana'}
newFruits = {'Rebecca':'Guava', 'Joshua':'Kiwi', 'Ronnie':'Papaya'}

# updates the dictionary by adding new key-value pairs. It can be done manually as well 
favFruits.update(newFruits)


# Returns a list containing a tuple for each key value pair
favFruits.items()


# Returns a list containing the dictionary's keys
favFruits.keys()


# Returns a list of all the values in the dictionary
favFruits.values


# Pops the last item/key-value pair
favFruits.popitem()


# Pops an element with a specific key. In this case, the key is 'Sam' 
favFruits.pop('Sam')


# copies the 'favFruits' dictionary into 'reservedFruits' dictionary. As dictionaries are mutable objects, 
# we need to copy the dictionary into another value and then do operations on them
reservedFruits = favFruits.copy()


# returns a dictionary with specific keys and a same value. If the value is not given then 'None' is assigned automatically
students = ('Adam', 'Saleh', 'Billah', 'Ramanov', 'Joseph')
dept = 'EEE'
studentsInfo = dict.fromkeys(students, dept)  # sudentsInfo dictionary have 5 keys named, Adam, Saleh, Billah, Ramanov and Joseph. Value of all of them is 'EEE'


# 
