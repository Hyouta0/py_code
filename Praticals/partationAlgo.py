
path = r"./MyWork_high/countrydata.csv";

contDict ={};
cnt =-1;
for contLine in open(path):
    if(cnt == -1):
        cnt+=1;
        continue;
    lineList = contLine.strip().split(",");
    if(lineList[2] in contDict):
        coutList = contDict[lineList[2]];
        coutList.append(contLine);
    else:
        contDict[lineList[2]] = [contLine];

#print(contDict);
comm_path =r"./MyWork_high/countrydat_CNT.csv";
for c,contList in contDict.items():
    myPath = comm_path.replace("CNT",c);
    fp = open(myPath,'a');
    for conuntry in contList:
        fp.write(conuntry);
    fp.close();

print("done");



