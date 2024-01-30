
sRec_path=r"./MyWork_high/student_rec.csv";
sMrk_path=r"./MyWork_high/student_mrk.csv";

stdRec_Dict= {};
cnt =-1;
for student in open(sRec_path):
    if(cnt == -1):
        cnt+=1;
        continue;
    id,name = student.strip().split(",");
    stdRec_Dict[id] = name;

cnt =-1;
for marks in open(sMrk_path):
    if(cnt == -1):
        cnt+=1;
        continue;
    id,eng,math,chem,phy,bio,pct,cls=marks.strip().split(",");
    if(stdRec_Dict[id]):
        print("student  "+stdRec_Dict[id]+" got ",pct,"% ");
