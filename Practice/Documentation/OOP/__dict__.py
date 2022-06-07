class employee:
    office = "Manru center, Chowhatta"
    boss = "Naved Ul Islam"
    hours = "9AM - 5PM"


shofiq = employee()
azad = employee()

shofiq.location, shofiq.hometown, shofiq.salary = "Subid bazar", "Dhaka", 50000   # creating instance variables
azad.location, azad.hometown, azad.salary = "Amberkhana", "Comilla", 65000        # creating instance variables

print(shofiq.__dict__)    # printing all changeable attributes of the object 'shofiq'
print(vars(azad))         # printing all changeable attributes of the object 'azad'

# __dict__ and vars() do the same job but __dict__ is comparatively faster. But sometimes vars() can be useful too