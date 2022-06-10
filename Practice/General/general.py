class Any:

    def printSomething(self):
        print("nothing")

    def printSomething(self, text):
        print(text)

    def printSomething(self, num1, num2):
        print("total: ", num1 + num2)



a = Any()

a.printSomething()

a.printSomething("is this working?")

a.printSomething(3,7)