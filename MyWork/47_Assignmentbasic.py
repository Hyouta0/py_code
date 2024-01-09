#read the file country data and find total population for continent using list and function.(function);

#path =r"~/code/py_code/PythonWork/Data/countrydata.csv";
path =r"../PythonWork/Data/countrydata.csv";
conList =[];
popList =[];
cnt=-1;
for country in open(path):
    if(cnt == -1):
        cnt+=1;
        continue;
    id,count,continent,pop,life,gdp=country.strip().split(",");
    if continent not in conList:
        conList.append(continent);
        popList.append(0);
    for i in range(len(conList)):
        if(conList[i] == continent):
            popList[i]+=float(pop);

for i in range(len(conList)):
    print("continent : ",conList[i]," total population : ",popList[i]);

