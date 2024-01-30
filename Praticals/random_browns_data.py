import random

#path where to Generate csv
pathW=r"./MyWork_high/student_Marks.csv";

name_list = ["nishad","kiran","harshal","sankat","soma","abhi","omkar","vivke","ganesh","prathick","viraj","nikhal","pd","prasad","faiz"];
#header of csv
hdr_line = "student_id,name,English,Math,chem,Phy,bio\n";
#open file in append mode
fp = open(pathW,"a");
#writhing data in file
fp.write(hdr_line);

sid =0;
#writing random marks to list of names
for name in name_list:
    sid+=1;
    line = str(sid)+","+name+","+str(random.randint(30,100))+","+str(random.randint(30,100))+","+str(random.randint(30,100))+","+str(random.randint(30,100))+","+str(random.randint(30,100))+"\n";
    fp.write(line);


fp.close();

