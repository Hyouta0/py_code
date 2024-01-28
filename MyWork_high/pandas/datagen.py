import os 
import random
import config as cfg

path =os.path.expanduser(cfg.Data.basePath+cfg.Data.fileNames)
pathW = f"./{cfg.Data.newFile}"
fp=open(pathW,'a')
cnt = -1

for line in open(path):
    if(cnt == -1):
        cnt+=1
        continue
    line = line.strip().split(',')
    fp.write(line[0]+','+line[1]+\
          ','+str(round(random.uniform(5.0,7.0),2))+\
          ','+str(round(random.uniform(54.0,90.0),1))+\
          ','+str(random.randint(20,60))+"\n"
          )

fp.close()
print("Done")

