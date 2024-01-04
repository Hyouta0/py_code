
class Emp:
    def __init__(self,empid,f_name,l_name,age,height,salary,mgnid):
        self.empid = empid;
        self.f_name = f_name;
        self.l_name = l_name;
        self.age = age;
        self.height =height;
        self.salary = salary;
        self.mgnid = mgnid;
    def Emp_print(self):
        print("                             manager id : ",self.mgnid);
        print("Employee id    : ",self.empid);
        print("Employee name  : ",self.f_name+" "+self.l_name);
        print("Employee age   : ",self.age," Employee height : ",self.height);
        print("Employee salary: ",self.salary);

path =r"./EmpData.csv";
cnt = -1;
empRec =[];

for emp in open(path):
    if(cnt == -1):
        cnt +=1;
        continue;
    id,fname,lname,age,hg,sal,mg=emp.strip().split(",");
    emp =Emp(id,fname,lname,age,hg,sal,mg);
    empRec.append(emp);

for emp in empRec:
    print("********************************************");
    emp.Emp_print();
    print("********************************************");
