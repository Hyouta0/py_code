
sRec_path =r"./MyWork_high/student_rec.csv";
sMrk_path =r"./MyWork_high/student_mrk.csv";

studRec=[];
cnt=-1;
for student in open(sRec_path):
    if(cnt == -1):
        cnt+=1;
        continue;

    id,name= student.strip().split(",");
    studList = [id,name];
    studRec.append(studList);

cnt=-1;
for marks in open(sMrk_path):
    if(cnt == -1):
        cnt+=1;
        continue;

    id,eng,math,chem,phy,bio,pct,cls = marks.strip().split(",");
    for student in studRec:
        if(id == student[0]):
            student.append(eng);
            student.append(math);
            student.append(chem);
            student.append(phy);
            student.append(bio);
            student.append(pct);
            student.append(cls);
            break;


print(studRec);
