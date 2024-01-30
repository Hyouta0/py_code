'''
numbers and alphabets: assign 3 alphabets for each digit between 0 and 9.
Write a program to write all possible codes that can be generated for any user entered number.
For example: 1 - a,b,c and 2 - d,e,f
then number 12 can be made as any of the codes: ad',ae',af',bd',be',bf',cd',ce',cf.
'''
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D']
'''
numDict = {}
idx=0
cnt=0
for i in alphe:
    if(idx == 3):
        idx=1
        cnt=cnt+1
    else:
        idx=idx+1
    if(cnt not in numDict):
        numDict[cnt]=[i]
    else:
        numDict[cnt].append(i)

print(numDict)

usr = input("Enter your number").strip()
usrNum = []
for i in usr:
    usrNum.append(int(i))
print(usrNum)

'''

    
