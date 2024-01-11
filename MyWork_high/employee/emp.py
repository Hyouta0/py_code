from salaryConfig import salaryDict 

class Emp:
    def __init__(self,id,fname,lname,age,height,salary,mgnid):
        self.id = id;
        self.f_name =fname;
        self.l_name =lname;
        self.age=age;
        self.height=height;
        self.salary=salary;
        self.mgnid=mgnid;

    def Emp_print(self):
        print("                             manager id : ",self.mgnid);
        print("Employee id    : ",self.id);
        print("Employee name  : ",self.f_name+" "+self.l_name);
        print("Employee age   : ",self.age," Employee height : ",self.height);

    def Emp_salDetail(self):
        print("Anually Salary : ",self.salary*12,".rs");
        print("Monthly Salaey : ",self.salary,".rs");
        print("+++++++++++++++++salary Distribution+++++++++++++++++")
        print("Basic Salary        : ",round(self.salary*salaryDict["basicSal"],2),".rs");
        print("House rent allowence: ",round(self.salary*salaryDict["hra"],2),".rs");
        print("City Allowence      : ",round(self.salary*salaryDict["cityAllowance"],2),".rs");
        print("Gratuity            : ",round(self.salary*salaryDict["gratuity"],2),".rs");

    def Emp_hearchi(self,companyRec):
        print("+++++++++++++++++Employee hearchi++++++++++++++++++++")
        self.Emp_recursion(self.id,companyRec,0);
        print(" ");


    def Emp_recursion(self,id,companyRec,lvl):
        if(id == 0):
            return;
        empObj = companyRec[id];

        if(lvl == 0):
            print(empObj.f_name+" "+empObj.l_name,end="");
        else:
            print("-->",empObj.f_name+" "+empObj.l_name,end="");

        if(empObj.id == empObj.mgnid):
            self.Emp_recursion(0,companyRec,lvl+1);
        else:
            self.Emp_recursion(empObj.mgnid,companyRec,lvl+1);


