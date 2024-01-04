import random

sRecPath = r"./MyWork_high/student_rec.csv";
sMrkPath =r"./MyWork_high/student_mrk.csv";

sRecHdr = "student_id,student_name\n";
sMrkHdr ="student_id,eng,math,chem,phy,bio,pct,class\n";


name_list = ["nishad","kiran","harshal","sankat","soma","abhi","omkar","vivke","ganesh","prathick","viraj","nikhal","pd","prasad","faiz"];

sRecFp = open(sRecPath,"a");
sMrkFp = open(sMrkPath,"a");

sRecFp.write(sRecHdr);
sMrkFp.write(sMrkHdr);

sid=0;
for name in name_list:
    sid+=1;
    sRecLine = str(sid)+","+name+"\n";
#eng ,math ,chem,phy,bio
    eng = random.randint(20,100);
    math = random.randint(20,100);
    chem = random.randint(20,100);
    phy= random.randint(20,100);
    bio = random.randint(20,100);
    pct = (eng+math+chem+phy+bio)*100/500;
    if(pct < 40):
        cls="FAIL";
    elif(pct < 50):
        cls="THIRD CLASS";
    elif(pct < 60):
        cls="SECOND CLASS";
    elif(pct < 70):
        cls="FIRST CLASS";
    else:
        cls="DENSCTION";
    sMrkLine = str(sid)+","+\
            str(eng)+","+\
            str(math)+","+\
            str(chem)+","+\
            str(phy)+","+\
            str(bio)+","+\
            str(pct)+","+\
            cls+"\n";

    sRecFp.write(sRecLine);
    sMrkFp.write(sMrkLine);

sRecFp.close();
sMrkFp.close();


