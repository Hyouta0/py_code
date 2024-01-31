
'''
start with hard coded list say a = [12,3,34,45,88,23,45,63,3,4,69,99] 
and find  maximum in this list (without using python readymade function)
'''
a = [12,3,34,45,88,23,45,63,3,4,69,99]
num = 0
for i in a:
    if(i > num):
        num = i
print(i)
