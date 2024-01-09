#read the file country data and find total population for continent using dictionary and function.

def total_population(path):
    cnt = -1;
    continentDict ={};
    for line in open(path):
        if(cnt == -1):
            cnt+=1;
            continue;
        id,country,continent,pop,life,gdp=line.strip().split(",");
        if continent in continentDict:
            continentDict[continent]+=float(pop);
        else:
            continentDict[continent] = float(pop);
    return continentDict;






path =r"../PythonWork/Data/countrydata.csv";
print(total_population(path));
