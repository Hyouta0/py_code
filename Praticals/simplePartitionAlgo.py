# read file country data sample
# count number of lines in the file.
# create 10 files where each file contains equal number or lines
# 5th file can have less number of lines.

path = r"./MyWork_high/countrydata.csv";

cnt=-1;
cntList =[];
for country in open(path):
    cnt+=1;
    if(cnt == 0):
        continue;
    cntList.append(country);
#print(cntList);

partLine = cnt//9;

comm_path=r"./MyWork_high/countrydata_NUM.csv";
fp_cnt = 1;
path =comm_path.replace("NUM",str(fp_cnt));
fp = open(path,'a');
cnt = 0;
for country in cntList:
    cnt+=1;
    if(cnt > partLine):
        cnt = 1;
        fp_cnt+=1;
        fp.close();
        fp = open(comm_path.replace("NUM",str(fp_cnt)),'a');
    fp.write(country);

fp.close();


