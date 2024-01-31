'''
start with hard coded list say 
,a = [12,3,34,45,88,23,45,63,3,4,69,99]
get two numbers from user, store them in second list.
Write a program to check if sencond list is subset of first list.
Print the output(DS and Algorithms)
'''
a = [12,3,34,45,88,23,45,63,3,4,69,99]
usrList =[]
for i in range(2):
    usrList.append(int(input("Enter num : ")))

a1 = False
a2 = False
for i in a:
    if usrList[0] == i :
        a1 = True
    if usrList[1] == i:
        a2 = True
if(a1 and a2):
    print(" list 2 is subset of a list ")
else:
    print("is not subset")
