path =r"./EmpData.csv";
cnt =-1;
companyList =[];
salaryDict ={
        "basicSal":0.35,
        "hra":0.175,
        "cityAllowance":0.428998333,
        "gratuity":0.016835
        };
def detailsal(line):
    monthlySal = int(line[5]);
    print("Emp Name           : ",line[1]+" "+line[2]);
    print("Emp Anual Salary   : ",monthlySal*12);
    print("Emp Monthly Salary : ",monthlySal);
    print("\n++++++++++++++++++salary Distribution+++++++++++++++++");
    print("Basic Salary       : ",round(monthlySal*salaryDict["basicSal"],3));
    print("HRA   Salary       : ",round(monthlySal*salaryDict["hra"],3));
    print("City Allowance     : ",round(monthlySal*salaryDict["cityAllowance"],3));
    print("Gratuity           : ",round(monthlySal*salaryDict["gratuity"],3));
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++");



for emp in open(path):
    if(cnt == -1):
        cnt+=1;
        continue;
    companyList.append(emp.strip().split(","));

while(1):
    ch = input("Enter any key /q to quit : ");
    if(ch == 'q'):
        break;
    id = input("Enter id of employee :").strip();
    flag = False;
    for empdata in companyList:
        if(id == empdata[0]):
            detailsal(empdata);
            flag =True;
            break;
    if(not flag):
        print("Employee not found with ",id);

