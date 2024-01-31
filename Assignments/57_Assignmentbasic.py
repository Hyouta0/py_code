'''
ask user to enter 10 numbers store them in list and print list,
count the number of times 10 is present in the list and print 
the result
'''
numList = []
cnt = 0
for i in range(10):
    num = int(input(f"Enter {i+1}th number : "))
    if(num == 10):
        cnt+=1
    numList.append(num)

print(f"list of number : {numList} \n10 has appered {cnt} times.")
