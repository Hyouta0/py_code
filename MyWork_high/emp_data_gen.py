# emp_id , first name ,last name ,age , hight, salary , manager id
import random

f_nameList=["kiran","nishad","harshal","sanket"];
l_nameList=["biradar","deshpande","bhandalkar","raskar"];
age=["5.11","5.5","5.9","6.0","6.5","6.9","7.0"];
empRec=[];

cnt=1;
for i in range(20):
    rndList = [cnt,random.choice(f_nameList),random.choice(l_nameList),random.randint(20,50),random.choice(age),random.randint(25000,600000),random.randint(1,cnt)];
    empRec.append(rndList);
    cnt+=1;

path = r"./EmpData.csv";
fp = open(path,'a');
hdr = "emp_id,first_name,last_name,age,hight,salary,manager_id\n";
fp.write(hdr);

for emp in empRec:
    empLine = str(emp[0])+","+emp[1]+","+emp[2]+","+str(emp[3])+","+emp[4]+","+str(emp[5])+","+str(emp[6])+"\n";
    fp.write(empLine);

fp.close();
print("Done");
