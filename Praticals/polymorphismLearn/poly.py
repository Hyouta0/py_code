import doctor
import engg

person_list = []

doc = doctor.Doctor("Nishad","Deshpande",22,"M","Eye")
person_list.append(doc)
eng = engg.Engg("kiran","Biradar",23,"M","cmp")
person_list.append(eng)

for per in person_list:
    per.printPerson()

