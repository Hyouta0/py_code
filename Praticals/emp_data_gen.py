# emp_id , first name ,last name ,age , hight, salary , manager id
import random


f_nameList=["kiran","nishad","harshal","sanket"];
l_nameList=["biradar","deshpande","bhandalkar","raskar"];


path = r"./EmpData.csv";
hdr = "emp_id,first_name,last_name,age,hight,salary,manager_id\n";
id =0;

fp = open(path,'a');
fp.write(hdr);
cnt = int(input("Enter no of data to be generated : "));

for i in range(cnt):
    id+=1;
    line = str(id)+","+\
            random.choice(f_nameList)+","+\
            random.choice(l_nameList)+","+\
            str(random.randint(20,50))+","+\
            str(round(random.uniform(5.0,7.0),2))+","+\
            str(random.randint(20000,100000))+","+\
            str(random.randint(1,id))+"\n";
    fp.write(line);

fp.close();
print("Done");
