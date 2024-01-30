
#brows the data
path=r"./MyWork_high/student_Marks.csv";
cnt = 0;
classRec = [];
for studentAttribute in open(path):
    cnt+=1;
    if(cnt == 1):
        continue;
    sid,sname,eng,math,chem,phy,bio = studentAttribute.strip().split(",");
    studRec = [int(sid),sname,float(eng),float(math),float(chem),float(phy),float(bio)]
    classRec.append(studRec);
#compute the data
for studRec in classRec:
    # id,name,eng    , math     , chem     , phy      , bio
    per = (studRec[2]+studRec[3]+studRec[4]+studRec[5]+studRec[6])*100/500;
    studRec.append(per);
    if(per <40):
        cls = "FAIL";
    elif(per < 50):
        cls = "THIRD CLASS";
    elif(per < 60):
        cls = "SECOND CLASS";
    elif(per < 70):
        cls ="FIRST CLASS";
    else:
        cls ="DISCTINCTION";
    studRec.append(cls);

#classification
pathW="./MyWork_high/student_result.csv";
hdrLine="student id,Name,English,Math,Chemical,Physics,Biology\n";
fs = open(pathW,"a");
fs.write(hdrLine);
for studRec in classRec:
    line = str(studRec[0])+","+studRec[1]+","+\
            str(studRec[2])+","+str(studRec[3])+","+str(studRec[4])+","+str(studRec[5])+","+str(studRec[6])+","+str(studRec[7])+","+\
            studRec[8]+"\n";
    fs.write(line);
fs.close();
print(classRec);

