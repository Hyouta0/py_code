
class Person:
    def __init__(self, fName, lName, age, gender):
        self.fName = fName
        self.lName = lName
        self.__age = age # private varible
        self._gender = gender #protected varible

    def printPerson(self):
        print(f"Name   : {self.fName} {self.lName}")
        print(f"Age    : {self.__age}")
        print(f"Gender : {self._gender}")


#p = Person("kiran","Biradar","23","M")
#p.printPerson()