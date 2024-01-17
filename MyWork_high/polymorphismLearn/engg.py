import person as p

class Engg(p.Person):
    def __init__(self,fName,lName,age,gender,exp):
        super().__init__(fName,lName,age,gender)
        self.exp = exp

    def printPerson(self):
        super().printPerson()
        print(f"Experties : {self.exp} ")




