# In this program, we'll be using @classmethod as an alternative constructor


class User:
    # actual constructor:
    def __init__(self, fName, lName, visits):   # usually to create an instance, we have to give 3 arguments named <fName>, <lName> and <visits>
        self.firstName = fName
        self.lastName = lName
        self.visits = visits

    # the alternative constructor:
    @classmethod
    def altConstructor(cls, user_info):                      # in this case, we have to give only one argument named <user_info>
        firstName, lastName, visits = user_info.split(" ")   # splitting the only argument string by the white spaces and keeping the values in 3 variables
        return cls(firstName, lastName, visits)              # returning a new instance of the class using the 3 variables as the arguments defined in the constructor


akram = User("akram", "khan", "165")
binoy = User("binoy", "kumar", "254")
sujit = User.altConstructor("sujit biswas 1044")

print(akram.__dict__)
print(binoy.__dict__)
print(sujit.__dict__)