from salaryConfig import salaryDict 

class Employee:
    def __init__(self,id,fname,lname,age,height,salary,mId):
        self.id = id 
        self.fName =fname 
        self.lName =lname 
        self.age=age 
        self.height=height 
        self.salary=salary 
        self.mId=mId 

    def printEmployee(self):
        print("                             manager id : ",self.mId) 
        print("Employee id    : ",self.id) 
        print("Employee name  : ",self.fName+" "+self.lName) 
        print("Employee age   : ",self.age," Employee height : ",self.height) 

    def employeeSalDetail(self):
        print("Anually Salary : ",self.salary*12,".rs") 
        print("Monthly Salaey : ",self.salary,".rs") 
        print("+++++++++++++++++salary Distribution+++++++++++++++++")
        print("Basic Salary        : ",round(self.salary*salaryDict["basicSal"],2),".rs") 
        print("House rent allowence: ",round(self.salary*salaryDict["hra"],2),".rs") 
        print("City Allowence      : ",round(self.salary*salaryDict["cityAllowance"],2),".rs") 
        print("Gratuity            : ",round(self.salary*salaryDict["gratuity"],2),".rs") 

    def empManagersLevel(self,companyRec):
        print("+++++++++++++++++Employee hearchi++++++++++++++++++++")
        self.employeeRecursion(self.id,companyRec,0) 
        print(" ") 


    def employeeRecursion(self,id,companyRec,lvl):
        if(id == 0):
            return 
        empObj = companyRec[id] 

        if(lvl == 0):
            print(empObj.fName+" "+empObj.lName,end="") 
        else:
            print("-->",empObj.fName+" "+empObj.lName,end="") 

        if(empObj.id == empObj.mId):
            self.employeeRecursion(0,companyRec,lvl+1) 
        else:
            self.employeeRecursion(empObj.mId,companyRec,lvl+1) 


