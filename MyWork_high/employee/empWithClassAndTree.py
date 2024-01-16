import emp

companyRec = {}
managerChildList = {}

path = r'../EmpData.csv'
cnt = -1

for line in open(path):
    if(cnt == -1):
        cnt+=1
        continue
    id,fName,lName,age,ht,sal,mId = line.strip().split(",")
    id  = int(id)
    age = int(age)
    ht  = float(ht)
    sal = float(sal)
    mId = int(mId)
    tmpEmp = emp.Employee(id,fName,lName,age,ht,sal,mId)
    companyRec[tmpEmp.id] = tmpEmp
    if(mId not in managerChildList):
        managerChildList[mId] = [id]
    else:
        managerChildList[mId].append(id)

def printHeriche(obj,companyRec,managerChildList):
    obj.printEmployee()
    print(f"Manager name   : {companyRec[obj.mId].fName} ")
    print("++++++++++++++++++++++++++++++++++++++++++++++")
    if(obj.id in managerChildList):
        for child in managerChildList[obj.id]:
            if(child != obj.id):
                printHeriche(companyRec[child],companyRec,managerChildList)

id = 1
printHeriche(companyRec[id],companyRec,managerChildList)
