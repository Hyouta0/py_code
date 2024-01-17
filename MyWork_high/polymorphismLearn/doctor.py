import person as p

class Doctor(p.Person):
    def __int__(self,fName, lName, age, gender, expertise):
        super().__init__(fName, lName, age , gender)
        self.expertise = expertise
    def printDoctor(self):
        super().printPerson()
        print("Experties : ",self.expertise)


d = Doctor("kiran","Biradar",23,"m","t")
d.printDoctor()