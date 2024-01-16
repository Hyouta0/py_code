import emp 

path =r'../EmpData.csv';
cnt =-1;
companyRec = {};
for line in open(path):
    if(cnt == -1):
        cnt+=1;
        continue;
    line = line.strip().split(',');
    tmpemp = emp.Employee(int(line[0]),\
            line[1],line[2],int(line[3]),\
            float(line[4]),int(line[5]),int(line[6]));
    companyRec[int(line[0])] = tmpemp;


while(1):
    exit=input("Enter any key /q to quit : ");
    if(exit.lower() == 'q'):
        break;
    id = int(input("Enter id to find details : "));
    if(id in companyRec):
        empObj = companyRec[id];
        empObj.printEmployee();
        empObj.employeeSalDetail();
        empObj.empManagersLevel(companyRec);
    else:
        print(f"{id} not found in data");
