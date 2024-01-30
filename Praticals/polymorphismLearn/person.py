class Person:
    def __init__(self,fName,lName,age,gender):
        self.fName = fName
        self.lName = lName
        self.__age   = age
        self._gender= gender
    def printPerson(self):
        print(f"Name : {self.fName} {self.lName}.")
        print(f"Age  : {self.__age} Gender : {self._gender}")


